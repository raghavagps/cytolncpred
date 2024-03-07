# **CytoLNCpred**
A computational method to predict the probability of lncRNA localizing to the cytoplasm
## Introduction
CytoLNCpred is a tool developed by Raghva-Lab in 2024. It is designed to predict the probability of lncRNA localizing to the cytoplasm. It utilizes a large language model - DNABERT-2 to make predictions. CytoLNCpred is also available as web-server at https://webs.iiitd.edu.in/raghava/cytolncpred. Please read/cite the content about the CytoLNCpred for complete information including algorithm behind the approach.

## PIP Installation
PIP version is also available for easy installation and usage of this tool. The following command is required to install the package 
```
pip install cytolncpred
```
To know about the available option for the pip package, type the following command:
```
cytolncpred -h
```
## Standalone
The Standalone version of CytoLNCpred is written in python3 and following libraries are necessary for the successful run:

- transformers==4.29
- argparse
- biopython
- torch
- numpy
- pandas

## Minimum USAGE
To know about the available option for the stanadlone, type the following command:
```
python cytolncpred.py -h
```
To run the example, type the following command:
```
python cytolncpred.py -i example_input.fa
```
This will predict the probability whether a submitted sequence will localize to the cytoplasm or nucleus. It will use other parameters by default. It will save the output in "outfile.csv" in CSV (comma separated variables).

## Full Usage
```
usage: cytolncpred.py [-h] -i INPUT [-o OUTPUT] [-m MODEL] [-t THRESHOLD] [-w WORKDIR]
                      [-d {1,2,3}]

```
```
Provide the following inputs for a successful run

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input: nucleotide sequence in FASTA format
  -o OUTPUT, --output OUTPUT
                        Output: File for saving results; by default outfile.csv
  -m MODEL, --model MODEL
                        Model path: Folder containing the fine-tuned DNABERT-2 model; by
                        default - dnabert2_10k
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold: Value between 0 to 1; by default 0.5
  -w WORKDIR, --workdir WORKDIR
                        Working directory: Directory where all intermediate and final files
                        will be created; by default .
  -d {1,2,3}, --display {1,2,3}
                        Display: 1:Cytoplasm-localized, 2: Nucleus-localized, 3: All; by
                        default 3
```

**Input File:** It allow users to provide input in the FASTA format.

**Output File:** Program will save the results in the CSV format, in case user does not provide output file name, it will be stored in "outfile.csv".

**Threshold:** User should provide threshold between 0 and 1, by default its 0.5.

**Working Directory:** Directory where intermediate files as well as final results will be saved

**Display type:** This option allow users to fetch either only lncRNA localizing to Cytoplasm by choosing option 1 or only lncRNA localizing to Nucleus by choosing option 2  or prediction for all lncRNAs by choosing option 2.

CytoLNCpred Package Files
=======================
It contains the following files, brief description of these files given below

INSTALLATION			: Installations instructions

LICENSE				: License information

README.md			: This file provide information about this package

dnabert2_10k.zip (not provided)			: This zipped file contains the fine-tuned DNABERT-2 model. It can be downloaded from the [link](https://webs.iiitd.edu.in/raghava/cytolncpred/downloads/dnabert2_10k.zip). This file should be present in the working directory. 

cytolncpred.py                  : Main python program

example.fasta	                : Example file contain lncRNA sequences in FASTA format

sample_output.csv		: Example output file for the program
