# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A Slovak diplomatic telegram sent to Berlin on 14 June 1940, catalogued as HCP128. Its cipher replaces ordinary letters with other letters.

Start with the [source catalogue or manuscript](https://crypto.hcportal.eu/dashboard/cryptograms/128). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

The saved candidate key gives a coherent partial Slovak reading about cement deliveries and fertilizer exports. Some source signs and a quantity remain unclear, and four unused cipher letters have no established values.

Open [Later source-checked literal](verification/readings/evidence/HCP128_Verified_Reading/plaintext_source_checked.txt) and the [research account](berlin-1940/README.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
sdejpolyakoviabypoziadalbergemana
```

This is the beginning of the saved output, with word spacing and accents omitted. The research account explains the proposed message in ordinary prose.

A passing replay does not decide every source sign, repair malformed words or recover the fertilizer quantity. Historical cleartext or another independently identified same-key message would be stronger evidence.

## Check one example by hand

1. Open the matching [ciphertext](verification/readings/evidence/HCP128_Verified_Reading/ciphertext_source_checked.txt) and [key](verification/readings/evidence/HCP128_Verified_Reading/key.csv). Count from the first character, using positions 1–3.

| Position | Recorded cipher letter | Candidate key gives |
| --- | --- | --- |
| 1 | `e` | `s` |
| 2 | `o` | `d` |
| 3 | `y` | `e` |

2. The [matching literal](verification/readings/evidence/HCP128_Verified_Reading/plaintext_source_checked.txt) begins `sde`. That checks the substitution, not the accuracy of the manuscript transcription.
3. Open the [source image](https://api.hcportal.eu/media/337/41991655394777.jpg) and compare the recorded cipher letters with the telegram itself. If you read a different sign, record that difference rather than changing the output to make a word fit.

Keep the three saved states separate: `initial` is the first saved transcription/output; `heldout_checked` records checking of the withheld continuation; `source_checked` adds later source corrections. Each ciphertext file has a plaintext file with the same suffix. Do not pair different states.

The first 335 positions helped fit the key; the last 121 were withheld from fitting. The full image had already been seen, so this was not a completely visually blind test. The four unseen cipher letters leave 24 equivalent completions of the unused alphabet slots.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/slovak-cipher-telegram-to-berlin-1940/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](berlin-1940/README.md) | Historical context, method, interpretation, credits and limits |
| [Later source-checked literal](verification/readings/evidence/HCP128_Verified_Reading/plaintext_source_checked.txt) | The saved text or bounded test result |
| [Matching source-checked ciphertext](verification/readings/evidence/HCP128_Verified_Reading/ciphertext_source_checked.txt) | The recorded input/assignments used in the example |
| [Frozen candidate key](verification/readings/evidence/HCP128_Verified_Reading/key.csv) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
