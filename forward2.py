# Given a matrix prints its contents row by row, separating the elements with tabs
def print_matrix(M):
	for row in M:
		line = ''
		for el in row:
			line = line + str(el) + '\t'
		print("%s\n"%line)



def Forward(seq, states, trans_p, emiss_p):
	########  INITIALIZE THE MATRIX  ########
	# Make the matrix
	Sq = '-' + seq + '-'
	# Create probability and pointer matrices
	F= [['*' for j in range(len(Sq))] for i in range(len(states))]
	# Initialise first row
	F[0][0] = 1
	for i in range(1, len(states)):
		F[i][0] = 0
	#Compile the matrix col by col, left to right
	########  		ITERATION 		 ########
	# Fill the matrix column by column
	for j in range(1, len(Sq) - 1):
		q_char = Sq[j]
		for i in range(len(states)):
			# Compute the sum over all the states
			res=0
			for k in range(len(states)):
				# Compute the p of transitioning from state k to i
				contribute = (F[k][j - 1]) * trans_p[k][i]  # multiply by transition
				res = res + contribute
			F[i][j]=round((res *emiss_p[i][H_emission_i[q_char]]),5)
	# End of matrices
	#########  		TERMINATION 		 ########
	# Fill in the last column
	for i in range(0, len(states)):
		res=0
		# Compute the sum over all the states
		for k in range(len(states)):
			# Compute the p of transitioning from state k to i
			contribute = (F[k][len(Sq)- 2]) * trans_p[k][i]  # multiply by transition
			res = res + contribute
			F[i][len(Sq) -1] ='{:.2e}'.format(res)

	return F, F[len(states) - 1][len(Sq) - 1]

if __name__ == '__main__':
	# Initial input
	seq = 'ATGCG'
	States = ['b','Y','N','e']
	transition_p =[[0, 0.2, 0.8, 0],
				   [0, 0.7, 0.2, 0.1],
				   [0, 0.1, 0.8, 0.1],
				   [0, 0, 0, 0]]
	emission_p = [[0.0, 0.0, 0.0, 0.0],
				[0.1, 0.4, 0.4, 0.1],
				[0.25, 0.25, 0.25, 0.25],
				[0.0, 0.0, 0.0, 0.0]]
	H_emission_i = {'A':0,'C':1,'G':2,'T':3}
	results = Forward(seq,States,transition_p,emission_p)
	F = results[0]
	print_matrix(F)
	print("the probability of the sequence %s given the model is %s" %(seq,str(results[1])))
