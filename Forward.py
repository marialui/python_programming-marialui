# Given a matrix prints its contents row by row, separating the elements with tabs
def print_matrix(M):
    for row in M:
        line = ''
        for el in row:
            line = line + str(el) + '\t'
        print("%s\n" % line)


# Computes the emission propability of the character seq(j) from state i
def emission_prob(i, j,emission,em_index,seq):
    row = i  # where i are the states
    col = em_index[seq[j]]
    return emission[row][col]


# here i means the state (in the rows)

# Compute the probability for the sequence up to seq(j) to be generated
# by a path ending in the state i, minus the emission probability factor
def fill_in(i, j,states,P,transition_prob):  # the function will return a value (the sum of all the probability of the previous column,
    # each is multiplied by its transition probability)
    res = 0
    # Compute the sum over all the states
    for k in range(len(states)):
        # Compute the p of transitioning from state k to i
        contribute = (P[k][j - 1]) * transition_prob[k][i]  # multiply by transition
        res = res + contribute
    return res


def forward(sequenza, states, transition_prob, emission, em_index):
    ########  INITIALIZE THE MATRIX  ########
    # Make the matrix
    Seq = '-' + sequenza + '-'  # this are the 2 extra character that are added
    P = [['*' for j in range(len(Seq))] for i in range(len(states))]
    P[0][0] = 1
    # Initialise the first column
    for i in range(1, len(states)):
        P[i][0] = 0
    ########  		ITERATION 		 ########
    # Fill the matrix column by column
    for j in range(1, len(Seq) - 1):
        for i in range(0, len(states)):
            # Compute the p of the sequence up to seq(j) in state i
            P[i][j] = round(fill_in(i, j,states,P,transition_prob) * emission_prob(i, j,emission,em_index,Seq), 5)  # multiply by emission
    ########  		TERMINATION 		 ########
    # Fill in the last column
    for i in range(0, len(states)):
        # Compute the p of the sequence up to seq(j) in state i
        P[i][len(Seq) - 1] = '{:.2e}'.format(fill_in(i, len(Seq) - 1,states,P,transition_prob))
    return P,P[len(states)-1][len(Seq) - 1],Seq


if __name__ == '__main__':
    # Initial input
    seq = 'ATGCG'
    # HMM Model
    states = ['b', 'Y', 'N', 'e']
    # Transition probabilities [states x states]
    transitions_prob = [[0, 0.2, 0.8, 0],
                        [0, 0.7, 0.2, 0.1],
                        [0, 0.1, 0.8, 0.1],
                        [0, 0, 0, 0]]
    # Transition probabilities index
    states_index = {'b': 0, 'Y': 1, 'N': 2, 'e': 3}
    # Emission probabilities [states x characters]
    emission = [[0.0, 0.0, 0.0, 0.0],
                [0.1, 0.4, 0.4, 0.1],
                [0.25, 0.25, 0.25, 0.25],
                [0.0, 0.0, 0.0, 0.0]]
    # Emission probabilities horizontal index
    h_emission_index = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
    results=forward(seq, states, transitions_prob, emission, h_emission_index)
    print(results[2])
    P= results[0]
    prob=results[1]
    print_matrix(P)
    print('Given the current model the probability of the sequence %s\n is %s' % (seq, prob))
