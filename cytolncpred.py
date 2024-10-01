import pandas as pd
import argparse
import numpy as np
import os
import zipfile
import subprocess
import sys
import pickle

nf_path = os.path.dirname(os.path.abspath(__file__))
# defining the function to check the seqeunce
def check_input_fasta(file_path, output_path):

	valid_nucleotides = set("ACGTUacgtu")
	is_sequence = False  # Flag to indicate we are reading sequence lines
	output = []  # Store the corrected FASTA lines
	headers = []  # Store headers
	sequences = []  # Store sequences
	current_sequence = []  # Temporary store for the current sequence
	try:
		with open(file_path, 'r') as file:
			for line_num, line in enumerate(file, start=1):
				line = line.strip()
                
				if not line:
					continue  # Skip empty lines

                # Check for header lines
				if line.startswith('>'):
					# Save the previous sequence if we have one
					if current_sequence:
						sequences.append("".join(current_sequence))
						current_sequence = []
                    
                    # Append header without the '>'
					headers.append(line[1:].strip())  
					output.append(line)  # Keep for corrected output
					if is_sequence:  # Valid end of the previous sequence
						is_sequence = False
					continue  # It's a valid header, move to the next line
                
                # Check sequence lines
				if not is_sequence:
					is_sequence = True  # We are now reading sequence lines
                
                # Validate sequence line
				if not all(char in valid_nucleotides for char in line):
					return False, f"Error at line {line_num}: Invalid character in sequence: {line}", None
                
                # Convert sequence to uppercase and replace 'U' with 'T'
				corrected_sequence = line.upper().replace('U', 'T')
				current_sequence.append(corrected_sequence)
				output.append(corrected_sequence)

            # Append the last sequence if the file ends with one
			if current_sequence:
				sequences.append("".join(current_sequence))

        # If no error, write the corrected output back to a new file
		with open(output_path, 'w') as outfile:
			outfile.write("\n".join(output) + "\n")
        
        # Create DataFrame with headers (without '>') and sequences
		df = pd.DataFrame({
			'Header': headers,
			'Sequence': sequences
		})
        
		return True, f"Multi-FASTA file format is correct. Corrected file saved as 'corrected_{file_path}'.", df
    
	except FileNotFoundError:
		return False, "Error: File not found.", None


def feature_gen(input, cell_line, outfile):
	if (cell_line==2)|(cell_line==6)|(cell_line==8)|(cell_line==10):
		args = ['-i', input, '-ft', 'PDNC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])
	elif (cell_line==3)|(cell_line==9):
		args = ['-i', input, '-ft', 'PKNC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])
	elif (cell_line==1)|(cell_line==13):
		args = ['-i', input, '-ft', 'PC_PDNC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])
	elif (cell_line==12)|(cell_line==15):
		args = ['-i', input, '-ft', 'PC_PTNC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])		
	elif cell_line==4:
		args = ['-i', input, '-ft', 'MAC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])
	elif cell_line==5:
		args = ['-i', input, '-ft', 'SC_PTNC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])
	elif cell_line==7:
		args = ['-i', input, '-ft', 'SC_PDNC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])			
	elif cell_line==11:
		args = ['-i', input, '-ft', 'TAC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path+'/Nfeature_DNA.py', *args])	
	else:
		args = ['-i', input, '-ft', 'DACC', '-o', outfile, '-path', sys.executable, '-p', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11', 'p12']
		subprocess.run([sys.executable, nf_path +'/Nfeature_DNA.py', *args])

def model_prediction(feature, cell_line):
	a = []
	df = pd.read_csv(feature)
	df.drop(columns=['Sequence_ID'], inplace=True)
	clf = pickle.load(open(nf_path+'/models/model'+str(cell_line)+'.pkl','rb'))
	y_p_score1=clf.predict_proba(df)
	y_p_s1=y_p_score1.tolist()
	a.extend(y_p_s1)
	df1 = pd.DataFrame(a).iloc[:,-1].round(3)
	df2 = pd.DataFrame(df1)
	df2.columns = ['ML Score']
	return df2

def main():
	parser = argparse.ArgumentParser(description='Provide the following inputs for a successful run')
	parser.add_argument("-i", "--input", type=str, required=True, help="Input: nucleotide sequence in FASTA format")
	parser.add_argument("-o", "--output",type=str, default="outfile.csv", help="Output: File for saving results; by default outfile.csv")
	parser.add_argument("-c", "--cell-line",type=int, choices=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], required=True, help="Select cell-line:\n"
			"1: A549\n"
			"2: H1.hESC\n"
			"3: HeLa.S3\n"
			"4: HepG2\n"
			"5: HT1080\n"
			"6: HUVEC\n"
			"7: MCF.7\n"
			"8: NCI.H460\n"
			"9: NHEK\n"
			"10: SK.MEL.5\n"
			"11: SK.N.DZ\n"
			"12: SK.N.SH\n"
			"13: GM12878\n"
			"14: K562\n"
			"15: IMR.90")
	parser.add_argument("-t","--threshold", type=float, default=0.5, help="Threshold: Value between 0 to 1; by default 0.5")
	parser.add_argument("-w", "--workdir",type=str, default="./", help="Working directory: Directory where all intermediate and final files will be created; by default .")
	parser.add_argument("-d","--display", type=int, choices = [1,2,3], default=3, help="Display: 1:Cytoplasm-localized, 2: Nucleus-localized, 3: All; by default 3")
	args = parser.parse_args()

	fasta_input = args.input
	output_file = args.output
	cell_line = args.cell_line
	thr = args.threshold
	wd = args.workdir
	disp = args.display
	

	print('\n======= Thanks for using CytoLNCpred. Your results will be stored in file :',output_file,' =====\n')

	input_file_name = os.path.basename(fasta_input)
	is_valid, message, seq_df = check_input_fasta(fasta_input, os.path.join(wd, 'corrected_' + input_file_name))
	if not is_valid:
		print(message)
		# Stop execution of the script if an error is found
		import sys
		sys.exit(1)

	feature_gen(os.path.join(wd, 'corrected_' + input_file_name), cell_line, os.path.join(wd, 'feature'))
	pred = model_prediction(os.path.join(wd, 'feature'), cell_line)
	pred['Seq ID'] = seq_df['Header']
	pred['Sequence'] = seq_df['Sequence']
	pred['Prediction'] = ['Cytoplasm' if pred['ML Score'][i]>thr else 'Nucleus' for i in range(0,len(pred))]
	pred = pred[['Seq ID','Sequence','ML Score','Prediction']]
	pred.to_csv(output_file, index=None)
	print("\n=========Process Completed. Cheers.=============\n") 
	os.remove(os.path.join(wd, 'feature'))
	os.remove(os.path.join(wd, 'corrected_' + input_file_name))
if __name__ == "__main__":
    main()
