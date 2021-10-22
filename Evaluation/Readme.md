# English - Swahili

## Data

- Data from Global voices. 

- Data split by 50-50 ratio. 1814 lines each - Dev and Test.

- link to the test and dev data
https://github.com/Freshia/Lafand/tree/main/data/new_aligned/split

- Domain is news

## Model

### EN-SW
- Link to the model
https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-sw/fine-tuned-jw300-baseline

### SW-EN
- Link to the model
https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/sw-en

## Results

BPE 35000 EN-SW
- 2021-10-19 00:31:46,912 - INFO - joeynmt.prediction dev bleu[13a]:  12.55 [Beam search decoding with beam size = 5 and alpha = 1.0]
- 2021-10-19 03:07:42,534 - INFO - joeynmt.prediction - test bleu[13a]:  12.96 [Beam search decoding with beam size = 5 and alpha = 1.0]

BPE 4000 SW-EN
- 2021-10-21 22:34:14,783 - INFO - joeynmt.prediction -  dev bleu[13a]:  12.93 [Beam search decoding with beam size = 5 and alpha = 1.0]
- 2021-10-21 22:39:16,704 - INFO - joeynmt.prediction - test bleu[13a]:  12.71 [Beam search decoding with beam size = 5 and alpha = 1.0]

