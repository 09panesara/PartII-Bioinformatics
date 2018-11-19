import random

def generate_hidden_sequence(state_mapping, transition_mtx):
    hidden_sequence = []

    # generate sample based on transition matrix probabilities
    sample_from = [[0 for i in range(int(row[0]*10))] + [1 for i in range(int(row[1]*10))] for row in transition_mtx]
    for row in sample_from:
        random.shuffle(row)

    curr_state = random.choice([0,1])
    hidden_sequence.append(curr_state)
    # Generate sequence of 50 states based on transition matrix
    for i in range(1, 50):
        curr_state = random.choice(sample_from[curr_state])
        hidden_sequence.append(curr_state)

    return([state_mapping[state] for state in hidden_sequence])

# hidden states S = {CpG, non-CpG}
hidden_states = ['CpG', 'nonCpG']
transition_mtx = [[0.5, 0.5], [0.4, 0.6]]
sequence = generate_hidden_sequence(hidden_states, transition_mtx)
print(sequence)
# ['nonCpG', 'CpG', 'CpG', 'CpG', 'CpG', 'CpG', 'CpG', 'CpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'CpG', 'nonCpG', 'nonCpG', 'CpG', 'CpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'CpG', 'CpG', 'CpG', 'nonCpG', 'CpG', 'nonCpG', 'CpG', 'CpG', 'nonCpG', 'nonCpG', 'CpG', 'CpG', 'CpG', 'CpG', 'nonCpG', 'nonCpG', 'nonCpG', 'nonCpG', 'CpG', 'CpG', 'nonCpG', 'CpG', 'CpG', 'CpG', 'CpG']

def generate_emission_sequence(hidden_sequence, emission_mtx, emission_symbols, hidden_states):
    sequence_length = len(hidden_sequence)
    no_emission_symbols = len(emission_symbols)
    no_hidden_states = len(hidden_states)
    hs_mapping = {key: i for i, key in enumerate(hidden_states)}

    sample_from = [[emission_symbols[emission_index]
                    for emission_index in range(no_emission_symbols)
                    for n in range(int(emission_mtx[state_index][emission_index]*10))]
                    for state_index in range(no_hidden_states)]

    emission_sequence = []
    for i in range(sequence_length):
        curr_state = hidden_sequence[i]
        emission_sequence.append(random.choice(sample_from[hs_mapping[curr_state]]))

    return emission_sequence

emission_mtx = [[0.2, 0.3, 0.3, 0.2], [0.3, 0.2, 0.2, 0.3]]
emission_symbols = ['A', 'C', 'G', 'T']
emission_sequence = generate_emission_sequence(sequence, emission_mtx, emission_symbols, hidden_states)
print(emission_sequence)
# ['T', 'G', 'A', 'A', 'G', 'C', 'G', 'G', 'C', 'C', 'T', 'T', 'T', 'A', 'T', 'A', 'A', 'A', 'T', 'A', 'C', 'A', 'A', 'A', 'A', 'T', 'A', 'A', 'A', 'T', 'A', 'C', 'C', 'A', 'T', 'C', 'T', 'T', 'G', 'T', 'A', 'C', 'A', 'A', 'A', 'A', 'G', 'C', 'G', 'C']