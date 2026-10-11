#!/usr/bin/env python3
"""Reproduce panels and arithmetic from saved manual judgments; does not read a cipher key."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_SHA = '8bc18278afc43ebde291e240e2f761c18aaa856c8d31f7ef0eedda5fc36c3a30'

def read(name):
    return json.loads((HERE / name).read_text())

def metrics(crops, observations):
    by_id = {q['id']: q for q in observations}
    if set(by_id) != {q['id'] for q in crops} or len(by_id) != len(observations):
        raise ValueError('IDs must match exactly and be unique')
    matrix = {label: {decision: 0 for decision in ('v', 'w', '?')} for label in ('v', 'w')}
    for crop in crops:
        obs = by_id[crop['id']]
        decision = obs['decision']
        if decision != '?':
            if not (obs['visible'] and obs['rgb_b_agree'] and obs['branch_at_least_2px']):
                raise ValueError('Committed call lacks visibility or branch evidence')
            if obs['basins'] != (1 if decision == 'v' else 2):
                raise ValueError('Committed call contradicts basin rule')
            crest_ratio = (obs['approx_crest_body_ratio_range'][0] if 'approx_crest_body_ratio_range' in obs and decision == 'w' else obs['crest_rise_px_approx'] / obs['body_height_px_approx'] if decision == 'w' else None)
            if decision == 'w' and crest_ratio < .25:
                raise ValueError('Committed w lacks minimum crest height')
        matrix[crop['label']][decision] += 1
    n = len(crops)
    called = sum(matrix[label]['v'] + matrix[label]['w'] for label in matrix)
    wrong = matrix['v']['w'] + matrix['w']['v']
    per_class = {label: (sum(matrix[label].values()) - matrix[label]['?']) / sum(matrix[label].values()) for label in matrix}
    return {'total': n, 'called': called, 'abstained': n-called, 'wrong_committed': wrong,
            'coverage': called/n, 'coverage_by_class': per_class,
            'agreement_among_committed': (called-wrong)/called if called else None,
            'confusion_against_prior_source_labels': matrix}

def calculate():
    cal = metrics(read('calibration_crops.json'), read('calibration_observations.json')['samples'])
    val = metrics(read('validation_crops.json'), read('validation_decisions_blinded.json')['samples'])
    stress = metrics(read('validation_crops.json'), read('stress_observations.json')['samples'])
    cal_ok = cal['wrong_committed'] == 0 and all(cal['confusion_against_prior_source_labels'][x][x] >= 3 for x in ('v','w'))
    val_ok = all(sum(val['confusion_against_prior_source_labels'][x].values()) >= 3 for x in ('v','w')) and val['wrong_committed'] == 0 and val['coverage'] >= .8 and min(val['coverage_by_class'].values()) >= .75
    review = read('independent_review.json')
    review_cal = metrics(read('calibration_crops.json'), [dict(q,visible=q['decision'] != '?') for q in review['calibration']])
    review_val = metrics(read('validation_crops.json'), [dict(q,visible=q['decision'] != '?') for q in review['validation']])
    review_ok = review_val['wrong_committed'] == 0 and review_val['coverage'] >= .8 and min(review_val['coverage_by_class'].values()) >= .75
    if review_ok != review['summary']['validation_gate']:
        raise ValueError('Independent review gate mismatch')
    target = read('target_observation.json')
    return {'source_sha256': SOURCE_SHA, 'protocol_sha256': hashlib.sha256((HERE/'protocol.md').read_bytes()).hexdigest(),
            'calibration': cal, 'calibration_gate_passed': cal_ok, 'validation': val,
            'operator_validation_gate_passed': val_ok, 'independent_calibration':review_cal,
            'independent_validation':review_val, 'independent_validation_gate_passed':review_ok,
            'experiment_acceptance_gate_passed':cal_ok and val_ok and review_ok and read('protocol_deviations.json')['controls_full_group_locators_frozen'] and target['visible'],
            'acceptance_failure_reasons':['Independent validation coverage fails','Control full-group locator requirement not fully implemented','Target discriminating stroke not securely visible'],
            'target_position':306, 'target_decision':target['decision'],
            'target_candidates':target['retained_candidates'], 'new_reading_proposed':False,
            'stress':stress, 'scope':'Arithmetic of saved manual source-shape judgments; no OCR, key replay or historical accuracy claim.'}

def render(source, out, phase):
    from PIL import Image, ImageDraw
    source_bytes = source.read_bytes()
    if hashlib.sha256(source_bytes).hexdigest() != SOURCE_SHA:
        raise ValueError('Source byte mismatch; stop')
    im = Image.open(source).convert('RGB')
    if im.size != (3024,4032):
        raise ValueError('Source dimension mismatch')
    if phase == 'calibration':
        crops = read('calibration_crops.json')
    elif phase in ('validation','stress'):
        crops = read('validation_crops.json')
    else:
        t = read('target_observation.json')
        crops = [dict(id='target306',bbox=t['bbox']),dict(id='group_locator',bbox=t['group_locator_bbox'])]
    out.mkdir(parents=True, exist_ok=True)
    hashes=[]
    # Individual views retain native pixels and exact 3x NN copies, with separate names.
    for q in crops:
        crop = im.crop(q['bbox'])
        hashes.append({'id':q['id'],'bbox':q['bbox'],'dimensions':list(crop.size),
                       'original_crop_raw_rgb_sha256':hashlib.sha256(crop.tobytes()).hexdigest()})
        if phase=='stress':
            ImageDraw.Draw(crop).rectangle((22,0,37,crop.height-1),fill=(160,160,160))
        prefix=out/(phase+'_'+q['id'])
        crop.save(str(prefix)+'_RGB_native.png')
        crop.getchannel('B').save(str(prefix)+'_B_native.png')
        for channel,view in [('RGB',crop),('B',crop.getchannel('B'))]:
            view.resize((crop.width*3,crop.height*3),Image.Resampling.NEAREST).save(str(prefix)+'_'+channel+'_3xNN.png')
    # Labels are omitted on all validation/target/stress panels.
    columns=5 if phase!='target' else 1
    cell_width=400 if phase!='target' else 1900
    cell_height=420
    panel=Image.new('RGB',(columns*cell_width,((len(crops)+columns-1)//columns)*cell_height),'white')
    draw=ImageDraw.Draw(panel)
    for i,q in enumerate(crops):
        x=i%columns*cell_width;y=i//columns*cell_height
        label=q['id']+((' '+q['label']) if phase=='calibration' else '')
        draw.text((x,y),label+(' SYNTHETIC OCCLUSION' if phase=='stress' else '')+' RGB | direct B; 3x NN',fill='black')
        crop=Image.open(str(out/(phase+'_'+q['id']))+'_RGB_3xNN.png')
        panel.paste(crop,(x,y+25));panel.paste(crop.getchannel('B'),(x+crop.width+15,y+25))
    panel.save(out/(phase+'_panel.png'))
    (out/(phase+'_crop_hashes.json')).write_text(json.dumps(hashes,indent=2)+'\n')
    return hashes

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path)
    p.add_argument('--out',type=Path)
    p.add_argument('--phase',choices=('calibration','validation','target','stress'))
    p.add_argument('--verify-recorded',action='store_true')
    args=p.parse_args()
    if args.phase:
        if args.source is None or args.out is None:p.error('--phase requires --source and --out')
        hashes=render(args.source,args.out,args.phase)
        print(json.dumps({'source_bytes_verified':True,'phase':args.phase,'crops':len(hashes),'out':str(args.out)},indent=2))
    else:
        result=calculate()
        if args.verify_recorded and result != read('results.json'):
            raise SystemExit('Recorded result mismatch')
        print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
