# 6 March 2019
# Viterbi algorithm but more modularised
#import gems as g


# Given a matrix prints its contents row by row, separating the elements with tabs
def print_matrix(M):
	for row in M:
		line = ''
		for el in row:
			line = line + str(el) + '\t'
		print("%s\n"%line)
#define a function that gived a list will extract the max value of the list
#and its position in the list.
def max_list_position(l):
	max_val = l[0]
	pos = 0
	for e in range(len(l)):
		if l[e]>max_val:
			max_val = l[e]
			pos = e
	return [max_val,pos]

#define a function that given a state i and a range of states k,j characters, a viterbi matrix and a transition matrix
#computes the maximum score (the best probability of emitting a j character from a state k and having transition to the state i)
# and store its value and its position.
def best_transition(i,j,states,trans_p,V):
	# Determine best transition to state i
	l = []
	for k in range(len(states)):
		contribute = V[k][j-1] * trans_p[k][i]
		l.append(contribute)
	best = max_list_position(l)
	return best


#define a function that given a sequence , a set of states, a transition matrix , an emission matrix and a dictionary for the emission:
#build 2 matrices V (probability matrix) and P(pointer matrix)

######initialization#######
#initialize the first column:
#put the element v[0][0]=1 and the others element of the first column equal 0

####iteration######
# #compile the matrix col by col, left to right:
#for each i state (row) of each j column:
# - for each k state, compute the probability of being at state k and emitting the character (j -1)
# and having transition to the state i
#-put those probabilities in a list and
#then find the maximum of these probability using the function best_transition
#in position V[i][j] (in the probability matrix) store the value of the best probability * the emission probability of emitting
#the character j at the state i
#in position P[i][j] the position of the best probability

#####termination#####
#for the last column compute the probabilities of emitting the character j -1 from a k state (not including begin
#and end state) and doing transition to the last state.
#find the higher probability and store its value in the V matrix : V[len(states)-1][len(sq)-1]
#Store its position in the P matrix:P[len(states)-1][len(sq)-1]

#then you have to traceback:
#initialize a variable path='e' when you will store all the state
# from the end one to begin following the optimal path
#starting from the last column P[i][j] of the matrix P where i=len state -1 and j =len seq +1
#read the content of the  cell[i][j]
#add the corrispondence state to path
#go to the other cell: P[cell][j-1]
#where i assumes the value of the P cell
#continue to traceback ntill you reach the cell [0][0]


#path: will be the variable that contains the best path for the sequence given the model
#the probability of the sequence given the path will be the last cell
#of the V matrix --> v[len states -1][len seq +1]

def Viterbi_M(sq,states,trans_p,emiss_p,h_emission_i):
	sq = '-' + sq + '-'
	# Create probability and pointer matrices
	V = [['*' for j in range(len(sq))] for i in range(len(states))] 
	P = [['*' for j in range(len(sq))] for i in range(len(states))] 
	# Initialise first row
	V[0][0] = 1
	for i in range(1,len(states)):
		V[i][0] = 0
	# Compile the matrix col by col, left to right
	for j in range(1,len(sq)-1):
		sq_char = sq[j]
		for i in range(len(states)):
			# Store probability and pointer
			best_trans = best_transition(i,j,states,trans_p,V)
			V[i][j] = best_trans[0] * emiss_p[i][h_emission_i[sq_char]]
			P[i][j] = best_trans[1]
	# End of matrices
	last_trans = best_transition(len(states)-1,len(sq)-1,states,trans_p,V)
	V[len(states)-1][len(sq)-1] = last_trans[0]
	P[len(states)-1][len(sq)-1] = last_trans[1]
	return [V,P]
			
def Traceback(sq,states,P):
	I = len(states)-1
	J = len(sq)+1
	path = 'e'
	while (I!=0) and (J!=0):
		cell = P[I][J]
		path = path + states[cell]
		J = J -1
		I = cell	
	return path[::-1]

if __name__ == '__main__':
	# Initial input
	seq = 'ATCGCGTGGT'
	States = ['b','Y','N','e']
	transition_p = [[0,0.2,0.8,0],
					[0,0.7,0.2,0.1],
					[0,0.1,0.8,0.1],
					[0,0,0,0]]
	emission_p = [[0,0,0,0],
				  [0.1,0.4,0.4,0.1],
				  [0.25,0.25,0.25,0.25],
				  [0,0,0,0]]
	H_emission_i = {'A':0,'C':1,'G':2,'T':3}
	# Compute the Viterbi and pointer matrices
	results = Viterbi_M(seq,States,transition_p,emission_p,H_emission_i)
	V = results[0]
	Ptr = results[1]
	print_matrix(V)
	print_matrix(Ptr)
	Viterbi_path = Traceback(seq,States,Ptr)
	print("the Viterbi path for the sequence %s\n is %s\n with a probability of %r"%(seq,Viterbi_path,'{:.2e}'.format(V[len(States)-1][len(seq)+1])))
