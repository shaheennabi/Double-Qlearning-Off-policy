from env import Environment
from policy import epsilon_greedy_behaviour_policy
from agent import Agent


def train_double_qLearning(iterations, rows, cols, num_actions, alpha, gamma, epsilon):
    env = Environment(rows=rows, cols=cols)
    agent = Agent(rows=rows, cols=cols, num_actions=num_actions, gamma=gamma, alpha=alpha)


    for _ in range(iterations):
        state = env.reset()
        done = False

        while not done: 
            combined_q_values = agent.Q_A[state] +  agent.Q_B[state]
            action = epsilon_greedy_behaviour_policy(combined_q_values, epsilon)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)

            state = next_state
    
    return agent


        
    

