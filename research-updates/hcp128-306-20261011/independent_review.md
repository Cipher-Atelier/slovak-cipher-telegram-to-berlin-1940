# Independent source-only procedural review: HCP128 position 306

Reviewed 11 October 2026 by a separate AI agent. **Outcome: abstain; preserve v/w.** My validation calls do not meet the frozen coverage thresholds, and the target independently lacks sufficiently secure discriminating-stroke visibility. This is AI procedural review, not independent human expert review.

## Evidence and exposure

I read only `protocol.md`, `calibration_crops.json`, and `validation_crops.json` from the experiment inputs. I did not read the key, plaintext, existing research prose, operator observations, operator blinded decisions, or later target/result/report files. The supplied protocol and metadata commit identifiers were c67d747 and fb75e46; I did not independently inspect Git history. The validation metadata contains labels: consequently this review is **not label-blind**, even though the enlarged panels displayed IDs only. No claim of blind replication is warranted.

I verified `/tmp/hcp128-306-original.jpg`: SHA-256 `8bc18278afc43ebde291e240e2f761c18aaa856c8d31f7ef0eedda5fc36c3a30`, dimensions 3024 × 4032, decoded RGB. I viewed the whole original RGB and direct B channel, native control crops, and labelled 3× nearest-neighbor RGB/B crops. Whole-image viewing necessarily provided a coarse view of all rows before sequential close inspection; it did not provide a virgin pixel holdout. I saved my calibration calls locally before enlarged validation inspection and my validation calls before enlarged target inspection. All pixel products remain under `/tmp/hcp128-306-independent/`; none are included in this deliverable. No OCR, sharpening, reconstruction, watermark subtraction, decipherment, or replay was performed.

The relevant text is typewritten. I interpreted “basins” as the lower turning points of the printed letter body, excluding horizontal serifs and adjacent letter ink. Measurements below are manual approximations, not fitted centerlines or precise pixel segmentation. For readable two-basin samples, the dark body branches appear wider than two original pixels at their distinguishable portions in both views. A ratio interval records a visibly substantial crest rather than a precisely localized measurement.

## Calibration calls from the frozen crops

| ID | Source label | Body basins | Approx. body height, original px | Crest/body | Decision | Visibility assessment |
|---|---|---|---|---|---|---|
| C5 | v | 1 | 35–42 | N/A | v | Continuous body and open interior; no second basin. |
| C17 | v | 1 | 33–40 | N/A | v | Continuous body and open interior. |
| C32 | w | 2 | 33–40 | 0.6–0.9 | w | Both minima and internal crest traceable. |
| C44 | w | 2 | 30–38 | 0.7–1.0 | w | Both minima and crest traceable. |
| C50 | w | 2 | 32–40 | 0.7–1.0 | w | Both minima and crest traceable. |
| C68 | v | 1 | 32–40 | N/A | v | Body and sufficient interior traceable. |
| C78 | w | 2 | 32–40 | 0.7–1.0 | w | Both minima and crest traceable. |
| C82 | v | 1 | 32–40 | N/A | v | Neighboring descender excluded; v body clear. |
| C140 | w | 2 apparent | 30–38 | Not admissibly measured | ? | Frozen right edge cuts the outer right terminal/body boundary; conservative abstention. |
| C145 | w | 2 | 32–40 | 0.7–1.0 | w | Both body basins traceable; right top serif is near the crop edge. |
| C176 | w | 2 | 32–40 | 0.6–0.9 | w | Both body basins traceable; left top serif is at the crop edge. |
| C183 | w | Incomplete in crop | 30–38 | Not admissibly measured | ? | Frozen left edge cuts into the first descending branch; neighboring i included. |
| C249 | w | 2 | 32–40 | 0.7–1.0 | w | Both minima and crest traceable. |

Calibration therefore has four readable v examples and seven readable w examples, zero committed disagreements with the supplied labels, and two abstentions. This meets the stated minimum of three readable examples per class. These are agreements with source transcription labels, not independent proof of historical ground truth.

I inspected wider source-only group context for C140, C145, C183 and, subsequently, C176 and C32 to audit crop boundaries. That context supports the clipping concerns; it does not repair the frozen crops or replace their decisions. No metadata coordinates were changed.

## Independent validation calls

| ID | Source label | Body basins | Approx. body height, original px | Crest/body | Decision | Visibility assessment |
|---|---|---|---|---|---|---|
| V01 | w | 2 | 32–40 | 0.6–0.9 | w | Both minima and internal crest traceable. |
| V02 | v | 1 | 32–40 | N/A | v | Continuous body and sufficient open interior. |
| V03 | v | 1 | 30–38 | N/A | v | Required body/interior clear; vertical watermark is to the right. |
| V04 | w | 2 | 32–40 | 0.6–0.9 | w | Required body clear; watermark lies above/right of it. |
| V05 | w | 2 | 32–40 | 0.6–0.9 | w | Both minima and crest traceable. |
| V06 | v | 1 | 32–40 | N/A | v | Continuous body and sufficient interior. |
| V07 | w | 2 apparent | 32–40 | Not admissibly measured | ? | Frozen left edge clips the outer upper descending body/terminal region. |
| V08 | w | 2 apparent | 32–40 | Not admissibly measured | ? | Diagonal watermark reaches the lower first basin; complete source-ink tracing is not secure. |
| V09 | v | 1 apparent | 32–40 | N/A | ? | Vertical watermark overlaps body/interior; unobscured exclusion of a second basin is not secure. |
| V10 | w | 2 | 32–40 | 0.6–0.9 | w | Both minima and crest traceable. |

Wider group views of V07 and V08 were inspected only after the validation calls were saved, as boundary/visibility checks. Their results did not change the frozen-crop decisions.

| Supplied class | Called v | Called w | Abstained | Coverage |
|---|---:|---:|---:|---:|
| v (4) | 3 | 0 | 1 | 75% |
| w (6) | 0 | 4 | 2 | 66.7% |
| Total (10) | 3 | 4 | 3 | 70% |

There are zero wrong committed calls against the supplied labels. The sample minimum is satisfied, but **70% overall coverage is below 80%, and 66.7% w coverage is below 75%**. Validation fails under this application of the frozen protocol. Abstentions are not counted as correct calls. These small, label-exposed counts are descriptive checks, not a statistical estimate of accuracy on obscured targets.

## Target visibility and decision

The supplied locator `[1405,1325,1700,1435]` contains a five-glyph typewritten group; the first glyph corresponds to the target crop `[1434,1325,1492,1435]`. This is a location check, not a decipherment or use of neighboring glyphs as training examples.

The target body is approximately 30–40 original pixels high. A vertical blue watermark band, approximately 15–20 original pixels wide excluding its thin border transitions, passes through its central/right body and the region needed to distinguish one basin from two. The direct B channel reduces the color contrast but retains the band and its borders; it does not provide recovered source ink. The views contain dark limb/minimum-like fragments, but I cannot securely assign a complete basin count or a qualifying internal crest from them. I cannot establish a continuous two-basin topology, nor sufficiently unobscured interior to exclude a second basin. A crest/body ratio would consequently be unjustified.

**Target decision: `?`, retain v/w.** This follows the target visibility rule independently of the validation failure. No new reading is proposed.

## Application limits and bounded next evidence

- The crop metadata supplies glyph boxes but no full-group locator boundaries. I cannot verify the protocol's requirement to record every control's independently located group locator, or independently check that the split includes every eligible singleton, using only these permitted inputs.
- Several boxes include neighbors or truncate outer strokes. Inclusion of a neighbor is manageable when its ink is clearly separate; truncation of a required branch is not. Any correction must be logged and cannot silently substitute corrected crops for this frozen-crop result.
- The criterion needs more precise operationalization for typewriting: which serif/body endpoint defines height, the baseline band, which centerline defines a printed crest, when a cropped terminal is harmless, and when watermark-overlapped ink remains sufficiently traceable. The readable controls are far above the 0.25 crest threshold, so they do not calibrate decisions near that boundary. I did not tune these definitions after viewing validation or the target.
- The whole-image view, exposed metadata labels, correlated typeface and shared watermark, and historical source-label uncertainty restrict independence. This review cannot certify the operator's earlier blind sequence, measurements, or files, which I did not read.
- A synthetic occlusion test can assess robustness only; it cannot restore the target or override this abstention. A better authorized scan or independent archival image is the relevant next evidence if the discriminating source stroke remains unavailable in these bytes.

No key, transcript, plaintext, uncertainty record, replay output, or other shared experiment file was modified by this review.
