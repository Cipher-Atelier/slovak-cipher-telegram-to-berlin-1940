# Berlin 1940: fixed-key heldout evidence for HCP128

Research status as of 5 October 2026: **coherent forward-substitution reading with a successful computational holdout; residual source errors and incomplete alphabet identification remain.**

## Research task

Read MZV message 6315/1940, addressed to Berlin on 14 June 1940, and test whether a key learned from an initial portion explains a withheld continuation. The source header reads *C 14 jún 456*. HCPortal places it in the Slovak National Archive, fond MZV, box 39. [Catalogue](https://crypto.hcportal.eu/dashboard/cryptograms/128), [source image](https://api.hcportal.eu/media/337/41991655394777.jpg).

## Tests completed

The first 335 positions formed the training portion; source-ambiguous positions 158 and 306 were masked. The last 121 positions were excluded from fitting. The full image had been displayed before this split, so this was a computational holdout rather than a perfectly visually blind experiment.

Three newly constructed, matched synthetic controls tested both text orientations. They selected the correct orientations and recovered 999/999 scored training letters and 363/363 withheld letters. Those numbers validate the experimental procedure on controls; they are not historical accuracy scores.

The target favored forward substitution, with sustained Slovak prose. No Madrid key was transferred. The selected key was frozen before formal transcription of the final 121 positions. Its unchanged application gave a coherent continuation about fertilizer exports. All 120 readable heldout source positions used mappings observed in training; position 428 remained unreadable. This is mapping coverage, not proof that 120 historical letters are individually correct.

Later source-only checks corrected four ciphertext readings: position 88 from e to a, 327 from m to n, 384 from i to f, and 411 from n to m. They did not change the key. Initial outputs and these post-test revisions must remain distinct.

## Result

The telegram concerns cement deliveries and fertilizer negotiations: three thousand wagonloads of cement for the year, the beginning of deliveries, a possible increase from one thousand to two thousand wagonloads, and fifteen hundred wagonloads of Thomas/basic-slag fertilizer. The subsequent ammonium-sulfate quantity remains corrupted and is not supplied here. The general cement/fertilizer subject was already visible in the catalogue, so topic agreement alone is not independent validation.

The post-correction frozen-key continuation reads:

`anaabyzakrocilvprotektorateouvolnenievyvozuumelychhnojivtisicpatstovagonovthomasovejmuckyast?cadesiacvagonovsiranuamoneho`

It begins inside the name spanning the training boundary. Spaces, accents, restored spelling and a polished translation would be editorial additions. Remaining source masks include positions 158, 306 and 428; other literal anomalies must not be silently repaired.

## What the key does and does not establish

All 22 observed cipher letters recur in the heldout portion. The four unobserved cipher letters, c, g, l and z, leave **24 equivalent completions** of the unused alphabet slots. The text therefore does not identify a unique complete 26-letter key. The observed mappings remain recovered hypotheses, not entries checked against a surviving historical key sheet.

The evidence supports a coherent reading of this telegram using forward substitution. It does not overturn the published general description of cipher C, which normally reverses the plaintext order.

## Unresolved questions

The remaining source signs, malformed words, exact sulfate quantity, some personal or institutional identifications, and unused alphabet entries remain open. An independently identified same-key message or historical cleartext would provide stronger verification. A bounded literature search did not locate an earlier exact reading, but no worldwide-priority claim follows from that result.

## Public sources and earlier-work credit

- [HCPortal HCP128](https://crypto.hcportal.eu/dashboard/cryptograms/128) and [digitized telegram](https://api.hcportal.eu/media/337/41991655394777.jpg), credited to the Slovak National Archive. Its public metadata still said “Not solved” on 5 October 2026.
- Eugen Antal, Pavol Zajac and Otokar Grošek, [“Diplomatic Ciphers Used by Slovak Attaché During the WW2”](https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf), HistoCrypt 2020, pp. 21–30, especially the description of cipher C on p. 22.

This is an AI-assisted research reading, not independent human expert certification. The source catalogue and earlier scholarship retain their own credit.
