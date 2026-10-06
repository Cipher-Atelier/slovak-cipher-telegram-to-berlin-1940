# Slovak cipher telegram to Berlin (14 June 1940)

A Slovak diplomatic telegram sent to Berlin on 14 June 1940, catalogued as HCP128. Its cipher replaces ordinary letters with other letters.

## What has been found?

The saved candidate key gives a coherent partial Slovak reading about cement deliveries and fertilizer exports. Some source signs and a quantity remain unclear, and four unused cipher letters have no established values.

A small example from the recorded result:

```text
sdejpolyakoviabypoziadalbergemana
```

This is the beginning of the saved output, with word spacing and accents omitted. The research account explains the proposed message in ordinary prose.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Later source-checked literal](verification/readings/evidence/HCP128_Verified_Reading/plaintext_source_checked.txt) to inspect the saved text or test result itself.
3. Read the [research account](berlin-1940/README.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/128); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

Coherent fixed-key partial continuation. Incomplete alphabet, prior full-image exposure, masks and three distinct saved states remain explicit.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/slovak-cipher-telegram-to-berlin-1940/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
