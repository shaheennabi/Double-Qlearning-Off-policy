import numpy as np

## behaviour policy

def epsilon_greedy_behaviour_policy(combined_q_values, epsilon):

    ## exploratory
    if np.random.rand() < epsilon:
        return np.random.randint(len(combined_q_values))
    
    else:
        return np.argmax(combined_q_values)