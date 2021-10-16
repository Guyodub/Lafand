### LAFAND-MT

A project to adapt low-resourced African languages machine translation models to the news domain.

### Swahili

### Stage One

The first stage of this project is building a parallel news corpus to be used to test the benchmark translation models, which were trained on Bibilical data.

This repo contains scripts to scrap and clean data from [Global Voices](https://sw.globalvoices.org/) to create a parallel news corpus for English to Kiswahili machine translation.

The raw data is contained [here](https://github.com/Freshia/Lafand/tree/main/data/raw)

The raw data was pre processed using the `text_alignment.py` script. The pre-processed data is stored [here](https://github.com/Freshia/Lafand/tree/main/data/aligned) 

#### Text Alignment

Run `alignment_check.py` to see if the two files are aligned. If they are not aligned, the script returns the number of lines that are misaligned, and a line where the misalignment has occured. 
With the help of this script, alignment can then be done manually by opening both files and editing the lines with the discrepancies.


### Stage Two

Testing the benchmark Masakhane models for [English to Swahili](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-sw) and [Swahili to English](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/sw-en) on the corpus created in stage one above.

### Stage Three

Train MT model on both [JW300](https://opus.nlpl.eu/JW300.php) data and [News Copus](https://opus.nlpl.eu/GlobalVoices.php) scrapped from Global Voices.