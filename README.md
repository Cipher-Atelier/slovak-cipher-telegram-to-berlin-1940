# Slovak cipher telegram to Berlin (14 June 1940)

A Slovak diplomatic telegram sent to Berlin on 14 June 1940, catalogued as HCP128. Its cipher replaces ordinary letters with other letters.

[Cipher Atelier](https://github.com/Cipher-Atelier) · [Research index](https://github.com/Cipher-Atelier/research-index) · [Reading guide](READING_GUIDE.md) · [Verification](verification/README.md)

## Current status — 11 October 2026

The saved candidate key gives a coherent partial Slovak reading about cement and fertilizer negotiations. All three saved states have 456 positions and three unresolved positions. Unobserved encrypted letters `c`, `g`, `l`, `z` leave 24 equivalent unused-alphabet completions; the complete historical alphabet is not identified.

| Evidence layer | Open this |
| --- | --- |
| Original | [HCP128 catalogue](https://crypto.hcportal.eu/dashboard/cryptograms/128) · [source image](https://api.hcportal.eu/media/337/41991655394777.jpg) |
| Recorded signs / candidate key | [Source-checked ciphertext](verification/readings/evidence/HCP128_Verified_Reading/ciphertext_source_checked.txt) · [key](verification/readings/evidence/HCP128_Verified_Reading/key.csv) |
| Literal | [Matching source-checked output](verification/readings/evidence/HCP128_Verified_Reading/plaintext_source_checked.txt) · [uncertainty ledger](verification/readings/evidence/HCP128_Verified_Reading/source_uncertainties.csv) |
| Interpretation | [Proposed message](berlin-1940/README.md#result) |

Positions 1–3 `e,o,y → s,d,e` give `sde`. [Check one example](READING_GUIDE.md#check-one-example-by-hand) with matching ciphertext/plaintext states; an initial ciphertext must not be paired with later output.

The [11 October source-shape experiment](research-updates/hcp128-306-20261011/README.md) did not resolve position 306: its independent validation gate failed, and the target remains `?`, with encrypted-source alternatives `v/w`. This negative result adds no deciphered letter. The separate [provenance follow-up](research-updates/hcp128-source-provenance-20261011.md) confirms a fonds reference, not an inventory entry or folio.

**Unresolved / missing:** positions 158, 306, 428, malformed wording, sulfate quantity and unused alphabet values remain. A better authorized cipher-page image, independent same-key text or historical cleartext is needed. No complete polished translation is included. The full image had been seen before the computational holdout split.

### Research update — 9 October 2026

Read the [new check and its limits](research-updates/2026-10-09-residual-audit.md). This update is documentation; new experiment scripts are not included.

## Start here

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Later source-checked literal](verification/readings/evidence/HCP128_Verified_Reading/plaintext_source_checked.txt) to inspect the saved text or test result itself.
3. Read the [research account](berlin-1940/README.md) for historical context, methods, earlier work and unresolved questions.

## Reproduce the checks

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/128); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

The standard-library baseline runs offline without extra packages. The [Evidence checks workflow](.github/workflows/verify.yml) runs it on Python 3.10 and 3.13 and checks the committed diff for whitespace errors.

## Research scope and limitations

Coherent fixed-key partial continuation. Incomplete alphabet, prior full-image exposure, masks and three distinct saved states remain explicit.

## Contribute

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/slovak-cipher-telegram-to-berlin-1940/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.

This is part of [Cipher Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

## Sources and rights

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.
