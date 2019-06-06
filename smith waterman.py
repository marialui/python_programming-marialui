
# Given a list returns the maximum value of the list and its position in it
def max_list_position(l):
	max_val = l[0]
	pos = 0
	for e in range(len(l)):
		if l[e]>max_val:
			max_val = l[e]
			pos = e
	return [max_val,pos]

# Given a matrix prints its contents row by row, separating the elements with tabs
def print_matrix(M):
	for row in M:
		line = ''
		for el in row:
			line = line + str(el) + '\t'
		print("%s\n"%line)


def highest_score_position(Matrix):
    m= len(Matrix) -1
    n= len(Matrix[0]) -1
    best_val = Matrix[m][n]
    best_position = [m,n]
    for row in range(len(Matrix)):
        for col in range(len(Matrix[row])):
            val = Matrix[row][col]
            if val>best_val:
                best_position = [row, col]
                best_val = val
    return best_position

def smith_waterman(sq1,sq2,d,subst_m,subst_i):
    S = [[0 for j in range(len(sq1) + 1)] for i in range(len(sq2) + 1)]
    P = [['*' for j in range(len(sq1) + 1)] for i in range(len(sq2) + 1)]
   
    for i in range(1, len(sq2) + 1):
        sq2_char = sq2[i - 1]
        for j in range(1, len(sq1) + 1):
            sq1_char = sq1[j - 1]
            # Compute the score for the cell coming from the left, up or diagonal
            side = S[i][j - 1] + d
            diag = S[i - 1][j - 1] + subst_m[subst_i[sq2_char]][subst_i[sq1_char]]
            down = S[i - 1][j] + d
            # Pick the best score
            max_score = max_list_position([side, diag, down])
            # Store best score and its position
            S[i][j] = max_score[0]
            P[i][j] = max_score[1]
            if max_score[0] < 0:
                S[i][j] = 0
                P[i][j]= '*'
    return [S, P]

def traceback(M,sq1,sq2,P):
    m= highest_score_position(M)[0]
    n= highest_score_position(M)[1]
    s = [m,n]  # position in P
    cell= P[s[0]][s[1]]
    M_val = M[s[0]][s[1]]  # content in cell in M(s)
    al1 = ''
    al2 = ''
# Initialise the new aligned sequences

# Traceback following the pointers ntill the maximum value of zero is reached,
# while building the alignment step-wise. # Build the alignment at position s
    while M_val !=0 and cell != '*':
        align = {0:[sq1[s[1]-1],'-'],
                 1:[sq1[s[1]-1],sq2[s[0]-1]],
                 2:['-',sq2[s[0]-1]]}
        al1 = al1 + align[cell][0]
        al2 = al2 + align[cell][1]
        # Move to next positon following the pointer
        move = {0: [0, -1], 1: [-1, -1], 2: [-1, 0]}
        s[0] = s[0] + move[cell][0]
        s[1]= s[1] + move[cell][1]
        cell = P[s[0]][s[1]]
    return [al1, al2]

def print_all(all):
    print (all[0][::-1] + '\n'+ all[1][::-1])


if __name__ == '__main__':
	# Initial input
	seqA = 'ACTGC'
	seqB = 'ATCC'
	D = -2
	substitution_m = [[2,-1,-1,0],
					  [-1,2,0,-1],
					  [-1,0,2,-1],
					  [0,-1,-1,2]]
	substitution_i = {'A':0,'C':1,'T':2,'G':3}
	# Compute the Score and Pointers matrices
	matrices = smith_waterman(seqA,seqB,D,substitution_m,substitution_i)
	Score = matrices[0]
	Pointers = matrices[1]
	print("Score matrix")
	print_matrix(Score)
	print("Pointers matrix")
	print_matrix(Pointers)


	print ('alignment:')
	print_all(traceback(Score,seqA,seqB,Pointers))



