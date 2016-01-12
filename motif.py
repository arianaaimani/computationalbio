import sys
import re
import numpy as np

alphabet = ['A', 'C', 'G', 'T']

def calculate_usefulness_of_motif(X, bound):
	true_pos = 0
	true_neg = 0
	false_pos = 0
	false_neg = 0

def qa(positive_data):
	consensus_sequence = []
	threshold = float(len(positive_data)) * 0.9
	for i in range(0,6):
		# Get ith letter for all words
		letters = [word[i] for word in positive_data]

		num_a = letters.count('A')
		num_c = letters.count('C')
		num_g = letters.count('G')
		num_t = letters.count('T')

		if (num_a >= threshold):
			consensus_sequence.append('A')
		elif (num_c >= threshold):
			consensus_sequence.append('C')
		elif (num_g >= threshold):
			consensus_sequence.append('G')
		elif (num_t >= threshold):
			consensus_sequence.append('T')
		elif(num_a + num_c >= threshold):
			consensus_sequence.append('AC')
		elif(num_a + num_g >= threshold):
			consensus_sequence.append('AG')
		elif(num_a + num_t >= threshold):
			consensus_sequence.append('AT')
		elif(num_c + num_g >= threshold):
			consensus_sequence.append('CG')
		elif(num_c + num_t >= threshold):
			consensus_sequence.append('CT')
		elif(num_g + num_t >= threshold):
			consensus_sequence.append('GT')
		else:
			consensus_sequence.append('ACGT')

	return consensus_sequence

def qb(positive_data, data):

	# Generate position weight matrix
	M = np.zeros(shape=(4,6))
	alphabet = ['A', 'C', 'G', 'T']
	num_sites = len(data)
	for i in range(4):
		for j in range(6):
			# Get jth letter for all words
			letters = [word[j] for word in positive_data]

			# # of sites with nucleotide i at position j
			num_i = letters.count(alphabet[i])

			M[i][j] = float(num_i) / num_sites
	print M




file1_neg = 'dataset1_negative.txt'
file1_pos = 'dataset1_positive.txt'
file2_neg = 'dataset2_negative.txt'
file2_pos = 'dataset2_positive.txt'

def main(file1, file2):
	print 'INPUT FILES: ' + file1 + ', ' + file2
	with open(file1) as f:
		negative_data = [line.replace('\n','') for line in f]
	with open(file2) as g:
		positive_data = [line.replace('\n','') for line in g]
	data = negative_data + positive_data

	seq_a = qa(positive_data)
	print 'QUESTION A: ' + str(seq_a)

	qb(positive_data, data)
	print 'QUESTION B:'

main(file1_neg, file1_pos)
main(file2_neg, file2_pos)
