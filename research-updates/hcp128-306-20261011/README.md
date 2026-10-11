# HCP128 position 306: source-shape experiment, 11 October 2026

Position 306 remains `?`, with finite source alternatives `v/w`. The fixed source-only
criterion gives different control coverage under separate reviewers (80% versus 70%);
independent validation fails. Neither reviewer can establish the covered central stroke
at row 7, group 5, glyph 1. No cipher key, transcript, plaintext or uncertainty
record was changed. No new decipherment is claimed.

## Evidence and frozen sequence

Base main was checked at `112e8380b4a4addcecab458596ddadb80e2ae479`, matching the task's
reference; no open issues or PRs were returned when checked. Project README,
verification instructions, CODEOWNERS, the organization contribution guide and research
workflow were read. The branch is a separate clone of the research repository.

The downloaded original JPG had the expected SHA-256
`8bc18278afc43ebde291e240e2f761c18aaa856c8d31f7ef0eedda5fc36c3a30`
and dimensions 3024 x 4032. The exact source is
https://api.hcportal.eu/media/337/41991655394777.jpg,
catalogue https://crypto.hcportal.eu/dashboard/cryptograms/128.
Images and crops remain local: no redistribution permission was inferred.

[Protocol](protocol.md) was saved in local commit `c67d747` before any pixels were
shown. Its SHA-256 is `90ddf9e367f41e76bc7652abf1f412ba1bd4650731012dd9e7ed4ce57b0ba5f3`.
Calibration was frozen in local commit `fb75e46` before validation pixels; opaque-ID
validation decisions were frozen in local commit `7fba419` before label reveal; target
abstention and [stress protocol](stress_protocol.md) were frozen in local commit
`7db2993` before synthetic stress panels. These are local procedural checkpoints,
not a public preregistration or independent proof of historical reader blindness.
Their contents are published together in this PR. The local checkpoints preserve
what was fixed when; remote publication does not retroactively make a preregistration.

The source is **typewritten**, discovered in the calibration locator, so the task's
"same hand" premise is better described as the same apparent typeface/impression.
The fixed geometric criterion was retained. Top padding for calibration rows 2 and 4
was expanded before validation to retain serifs; split and classification rules did not
change. Exact final sample coordinates are saved, as are raw RGB crop fingerprints.

## Results

| Stage | Prior source labels | Committed calls | Abstentions | Wrong committed calls | Coverage |
|---|---:|---:|---:|---:|---:|
| Calibration, rows 1/2/4/6 | 4 v, 9 w | 13 | 0 | 0 | 100% |
| Operator validation, whole rows 3/5 | 4 v, 6 w | 8 | 2 | 0 | 80% |
| Independent calibration, same crops | 4 v, 9 w | 11 | 2 | 0 | 84.6% |
| Independent validation, same crops | 4 v, 6 w | 7 | 3 | 0 | 70% |
| Synthetic 16px occlusion, same consumed validation | 4 v, 6 w | 0 | 10 | 0 | 0% |

Operator validation class coverage was 3/4 v (75%) and 5/6 w (83.3%), meeting the frozen
80% overall, 75% per-class and zero-wrong-call gates exactly at the overall/v boundary.
The uncalled controls were position 127 (diagonal band through left valley) and 212
(vertical band through interior). Agreement is against existing source-only labels,
not independent historical ground truth. These small samples provide no reliable
historical accuracy estimate; conditional agreement among eight calls is 100%, while
unconditional coverage is 80%.

[Target observation](target_observation.json): two dark lower lobes appear, but the
vertical band and its edge lines intersect the central body required to determine
valleys/crest. RGB and direct B channel views retain this contamination. The visibility
rule requires abstention. The band's colour core is 16px wide, x=[1456,1472), measured
in a blank area above the glyph; edge lines extend beyond that core. No claim is made
that the stroke was destroyed in the archival original, only that these bytes do not
establish uncontaminated topology under this protocol.

The prespecified next step was completed as a stress test: opaque deletion of 16
columns at the same crop-relative offset produced ten abstentions. This is a
conservative information-loss test, not a physical model of a translucent watermark,
not fresh validation and not evidence for either target letter. Zero wrong calls here
is accompanied by **zero coverage**, with conditional agreement undefined.

The [independent review](independent_review.md) abstained additionally at validation
V07 (position 120) because its outer branch is clipped, giving 70% overall and 66.7% w
coverage: **the independent validation gate fails**. It also rejected calibration C140
and C183 as clipped. These disagreements are retained, not resolved by changing boxes
or choosing the higher score. The target abstention is shared. The method is therefore
not independently validated for a new reading. AI agreement is not human expert review.
CODEOWNERS still requires founder review before a research change is accepted.

## Reproduce

Python 3.10+ runs saved-judgment arithmetic without third-party packages:

```sh
python3 research-updates/hcp128-306-20261011/run_experiment.py --verify-recorded
```

Expected operator counts are 13/13, 8/10 and 0/10 committed calls; independent
counts are 11/13 and 7/10. Independent validation fails, target `?`, candidates v/w.
This command checks computation from human-readable saved manual observations; it
cannot regenerate those perceptual judgments automatically.

For pixel review, separately obtain the authorized JPG from its provider, respecting
its terms. Install Pillow if absent (tested Pillow version recorded in environment.json).
Pass the JPG path and an output directory **outside the repository**:

```sh
python3 research-updates/hcp128-306-20261011/run_experiment.py --source /path/to/41991655394777.jpg --out /tmp/hcp128-306-review --phase calibration
python3 research-updates/hcp128-306-20261011/run_experiment.py --source /path/to/41991655394777.jpg --out /tmp/hcp128-306-review --phase validation
python3 research-updates/hcp128-306-20261011/run_experiment.py --source /path/to/41991655394777.jpg --out /tmp/hcp128-306-review --phase target
python3 research-updates/hcp128-306-20261011/run_experiment.py --source /path/to/41991655394777.jpg --out /tmp/hcp128-306-review --phase stress
```

The script rejects a source hash/dimension mismatch and generates native RGB/B,
3x nearest-neighbor views, labelled panels and raw RGB crop hashes. It uses no OCR,
restoration, key, plaintext, or network requests. Validation panels omit source labels.
Compare the raw RGB crop hashes with [crop fingerprints](crop_fingerprints.json).
Do not inspect validation/target until independently freezing calibration calls if
repeating the procedural split. Existing metadata was already visible to the main
operator, so the opaque IDs are label concealment, not strong blinding.

The supported baseline command `python3 verification/check_all.py` was run once as
an unchanged-evidence regression check and passed (27 files); that replay is not the
new experiment. `git diff --check` and the new arithmetic verifier passed. The original
SHA256SUMS inventory and all original evidence bytes are untouched; the new package
has its own SHA256SUMS.txt inventory.

## Limits and next source step

The intended independently located full-group controls were not fully implemented:
control boxes were approximated from calibration row locators and typewriter pitch;
no full-group locator for every control was frozen. Several boxes truncate outer ink.
This is a protocol deviation, recorded in protocol_deviations.json, not a claimed
successful full-group sample audit. Corrected crops would be a later, nonblind test.
Operator scalar crest heights are rounded representative estimates of a visually
large crest (about 0.75 body height), not independently traced pixel landmarks. The
independent reviewer supplied ranges; no near-threshold crest was calibrated.

Prior whole-image exposure in the older work and the new operator's metadata exposure
(including the older preference v) remain explicit. Approximate manual heights are
not high-precision pixel measurements; their purpose is a conservative shape gate.
The script makes sample extraction and metric arithmetic repeatable; independent
perceptual review still needs legal access to the linked source image.

Repeating enhanced views of the same pixels cannot justify a forced source reading.
The useful next step is an authorized image without the added watermark, a better
archival scan, or independent source-reader review of the same coordinates. No request
was sent to an institution or person. The fixed key and all three unresolved positions
remain as before; position 428 was not investigated by this experiment.

Codex assisted protocol design, source-pixel inspection, scripts and reporting. A
separate Codex agent reviewed the source-only criteria and controls. Earlier source
transcriptions and their singleton labels are credited to the project evidence at the
base commit. This package claims only a bounded negative source-reading result.
