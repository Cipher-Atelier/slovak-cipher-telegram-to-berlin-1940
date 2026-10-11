# Frozen source-only protocol: HCP128 position 306

Frozen before any scan pixels were displayed in this experiment, 11 October 2026.
Base: 112e8380b4a4addcecab458596ddadb80e2ae479. Target: physical row 7,
group 5, glyph 1, transmitted position 306. Source JPG:
https://api.hcportal.eu/media/337/41991655394777.jpg
SHA-256: 8bc18278afc43ebde291e240e2f761c18aaa856c8d31f7ef0eedda5fc36c3a30;
3024 x 4032. Coordinates are original pixels [left, top, right, bottom), no deskew.

## Exposure and forbidden evidence

The operator has read repository descriptions, source transcription metadata (including
the old visual preference v), and the task's v/w candidates. This is not a wholly blind
historical reading. The key and plaintext files will not be opened or used to decide
shape. Existing source-only singleton v/w labels identify controls, not historical ground
truth. Controls below are new procedural row holdouts, not virgin historical holdouts.
No OCR, generated reconstruction, sharpening, inpainting or watermark subtraction.
Images/crops stay local because redistribution permission is not established.

## Split fixed from source metadata, before pixel inspection

Calibration: every singleton v/w in physical rows 1, 2, 4, 6.
Whole-row validation: every singleton v/w in physical rows 3 and 5.
No validation pixels or target pixels inspected until calibration measurements are saved.
Row 7 is reserved for target inspection; its other glyphs cannot train the decision rule.
Each glyph is cropped from an independently located full group; locator boundaries are
recorded. Validation panels use opaque sample IDs and reveal labels only after decisions.
Any later coordinate correction must be recorded and cannot change split or criteria.

## Shape criteria fixed in advance

Count *body* basins of the ink stroke, ignoring connecting entry/exit flourishes. A basin
is a descending then ascending stroke reaching the baseline band. A w requires two
basins separated by an internal ascending/descending crest. The crest must rise at
least 0.25 of body height above the higher of its two flanking minima, and each branch
must remain traceable as source ink (at least 2 original pixels wide where distinguishable
from background). A v requires one basin with a traceable continuous descending and
ascending body, AND sufficient unobscured interior to exclude a qualifying second basin.
Width or resemblance alone is insufficient; joined writing and neighboring letters cannot
be counted as a second basin. Unclear boundaries, a missing discriminating stroke,
watermark interference with that stroke, or disagreement of RGB and direct B channel
on the required topology => abstain ?. Body heights and crest differences are manual
approximate original-pixel measurements; do not assert subpixel precision.

Use native RGB, direct B channel, and labelled 3x nearest-neighbor copies only. These
are views of existing pixels, not restored evidence. For any sample record basin count,
crest/body ratio when applicable, visibility and decision. Calibration must establish
at least 3 readable examples per class with no committed wrong calls. If unavailable,
stop classification and preserve v/w. Freeze calibration observations before validation.

## Acceptance and stopping

Validation must contain at least 3 labelled examples per class. Require zero wrong
committed calls, at least 80% coverage overall and at least 75% in each class. Abstentions
count against coverage, not as correct calls. Publish counts, confusion table, and
class coverage. Failure means no target resolution with this protocol; no tuning after
seeing validation or target results. Inspect target even on failure to record source gap,
but no promoted reading. Even on passing validation, target must independently satisfy
all shape/visibility criteria. An independent reviewer must confirm protocol application
and target shape before any new reading is proposed. AI agreement is not human expert
review. The saved key, transcript, plaintext, uncertainties and replay expected output
stay unchanged. A negative result is a completed experiment.

## Next bounded step

If target remains obscured, test whether the same frozen criterion can survive a local
synthetic vertical occlusion on validation controls, using the target's measured band
width; label it a stress test, never a reconstruction. Do not use it to override abstention.
If the distinguishing stroke is absent from these bytes, a better authorized scan or
independent archival image is the necessary next source evidence.
