import sys
import re

# ANSWER: CGATAT

'''
	Given a file and consensus sequence, find 
	number of times sequence occurs
'''
def find_number_occurences(consensus_sequence, file_content):
	num = re.findall(consensus_sequence, file_content)
	return len(num)

'''
	Return consensus sequence given 2 files:
	file1 contains binding sequences, and file2
	contains non-binding sequences
'''
def get_consensus_sequence(file1, file2):

	best_sequence = ''
	best_sequence_score = 0
	scores = {}

	# Read files
	my_file1 = open(file1)
	my_file1_contents = my_file1.read()
	my_file2 = open(file2)
	my_file2_contents = my_file2.read()

	# Alphabet for constructing consensus sequences
	nucleotides = ['A', 'C', 'G', 'T', 'AC', 'AG', 'AT', 'GC', 'CT','GT','ACGT']

	# Non-variable consensus sequence
	for i in range(0, 4):
		for j in range(0,4):
			for k in range(0,4):
				for l in range(0,4):
					for m in range(0,4):
						for n in range(0,4):
							seq = nucleotides[i] + nucleotides[j] + nucleotides[k] + nucleotides[l] + nucleotides[m] + nucleotides[n]

							
							if (len(seq) == 6):
								# Find N = # of times w appears in file1
								N = find_number_occurences(seq, my_file1_contents)

								# Find K = # of times w appears in file2
								W = find_number_occurences(seq, my_file2_contents)

								scores[seq] = [N, W]
								ratio = float(N)/W
								#ratio = float(N+1)/(W+1)
								print '{' + seq + '}: ' + str(N) + ' ' + str(W) + ' ' + str(ratio)

								if ratio > best_sequence_score:
									best_sequence_score = ratio
									best_sequence = seq

	# Variable consensus sequence
	for i in range(0, 11):
		for j in range(0, 11):
			for k in range(0, 11):
				for l in range(0, 11):
					for m in range(0, 11):
						for n in range(0, 11):
							
							# Find all possible consensus sequences
							num_var_seqs = (i+1)*(j+1)*(k+1)*(l+1)*(m+1)*(n+1)
							if num_var_seqs <= 6:
								continue

							var_seqs_score = 0
							var_seqs_N = 0
							var_seqs_W = 0
							for a in range(0, len(nucleotides[i])):
								for b in range(0, len(nucleotides[j])):
									for c in range(0, len(nucleotides[k])):
										for d in range(0, len(nucleotides[l])):
											for e in range(0, len(nucleotides[m])):
												for f in range(0, len(nucleotides[n])):
													var_seq = nucleotides[i][a] + nucleotides[j][b] + nucleotides[k][c] + nucleotides[l][d] + nucleotides[m][e] + nucleotides[n][f]
													var_seqs_N += scores[var_seq][0]
													var_seqs_W += scores[var_seq][1]

							var_seqs_score = float(var_seqs_N)/var_seqs_W
							#var_seqs_score = float(var_seqs_N + 1)/(var_seqs_W + 1)
							if var_seqs_score > best_sequence_score:
								best_sequence_score = var_seqs_score
								best_sequence = '{' + nucleotides[i] + ',' + nucleotides[j] + ',' + nucleotides[k] + ',' + nucleotides[l] + ',' + nucleotides[m] + ',' + nucleotides[n] + '}'

							print '{' + nucleotides[i] + ',' + nucleotides[j] + ',' + nucleotides[k] + ',' + nucleotides[l] + ',' + nucleotides[m] + ',' + nucleotides[n] + '}: ' + str(var_seqs_score)

						


	print 'BEST: ' + str(best_sequence_score) + ' ' + best_sequence
						

# Read GATA2 input files if necessary
gata2_chr1_file = 'GATA2_chr1.fa'
not_gata2_chr1_file = 'not_GATA2_chr1.fa'
arguments = len(sys.argv)
if (arguments == 3):
	gata_2_chr1_file = sys.argv[1]
	not_gata2_chr1_file = sys.argv[2]
elif (arguments > 3):
	print 'Error'
	sys.exit(0)
get_consensus_sequence(gata2_chr1_file, not_gata2_chr1_file)



