# **CytoLNCpred**
A computational method to predict the probability of lncRNA localizing to cytoplasm
## Introduction
CytoLNCpred is a tool developed by Raghava-Lab in 2024. It is designed to predict the probability of lncRNA localizing to the cytoplasm. It utilizes a correlation-based features with machine learning to make predictions. CytoLNCpred is also available as web-server at https://webs.iiitd.edu.in/raghava/cytolncpred. Please read/cite the content about the CytoLNCpred for complete information including algorithm behind the approach.

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
- numpy  2.1.1
- pandas  2.2.3
- scikit-learn  1.5.2
- xgboost  2.1.1
- argparse

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
usage: cytolncpred.py [-h] -i INPUT [-o OUTPUT] -c {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15} [-t THRESHOLD] [-w WORKDIR] [-d {1,2,3}]

```
```
Provide the following inputs for a successful run

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input: nucleotide sequence in FASTA format
  -o OUTPUT, --output OUTPUT
                        Output: File for saving results; by default outfile.csv
  -c {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}, --cell-line {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
                        Select cell-line: 1: A549 2: H1.hESC 3: HeLa.S3 4: HepG2 5: HT1080 6: HUVEC 7: MCF.7 8: NCI.H460 9: NHEK 10: SK.MEL.5 11: SK.N.DZ 12:
                        SK.N.SH 13: GM12878 14: K562 15: IMR.90
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold: Value between 0 to 1; by default 0.5
  -w WORKDIR, --workdir WORKDIR
                        Working directory: Directory where all intermediate and final files will be created; by default .
  -d {1,2,3}, --display {1,2,3}
                        Display: 1:Cytoplasm-localized, 2: Nucleus-localized, 3: All; by default 3
```

**Input File:** It allow users to provide input in the FASTA format.

**Output File:** Program will save the results in the CSV format, in case user does not provide output file name, it will be stored in "outfile.csv".

**Threshold:** User should provide threshold between 0 and 1, by default its 0.5.

**Cell-line:** User should select the specific cell-line among the 15 cell-lines for which prediction will be done.

**Working Directory:** Directory where intermediate files will be saved

**Display type:** This option allow users to fetch either only lncRNA localizing to Cytoplasm by choosing option 1 or only lncRNA localizing to Nucleus by choosing option 2  or prediction for all lncRNAs by choosing option 2.

CytoLNCpred Package Files
=======================
It contains the following files, brief description of these files given below

INSTALLATION			: Installations instructions

LICENSE				: License information

README.md			: This file provide information about this package

Nfeature_DNA.py  : This file is used to compute the features

model : This folder contains the pickled models for each cell-line

cytolncpred.py                  : Main python program

example.fasta	                : Example file contain peptide sequences in FASTA format

sample_output.csv		: Example output file for the program
