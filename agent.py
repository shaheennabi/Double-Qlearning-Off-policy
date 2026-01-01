import numpy as np

class Agent:
    def __init__(self, rows, cols, num_actions, gamma, alpha):
        self.rows = rows
        self.cols = cols 
        self.num_actions = num_actions
        self.gamma = gamma
        self.alpha = alpha

        self.Q_A = np.zeros((rows, cols, num_actions))
        self.Q_B = np.zeros((rows, cols, num_actions))



    def update(self, current_state, action, reward, next_state, done):
        row, col = current_state
        new_row, new_col = next_state
        
        ## select which q_value to update
        if np.random.rand() < 0.5:
            ## update Q_A
            best_action = np.argmax(self.Q_A[new_row, new_col])

            target = reward
            
            if not done:
                target += self.gamma *  self.Q_B[new_row, new_col, best_action]

            td_error = target - self.Q_A[row, col, action]
            self.Q_A[row, col, action] += td_error * self.alpha
        else:
            ## update Q_B
            best_action = np.argmax(self.Q_B[new_row, new_col])
            target = reward

            if not done:
                target += self.gamma * self.Q_A[new_row, new_col, best_action]

            td_error = target - self.Q_B[row, col, action]
            self.Q_B[row, col, action] += td_error * self.alpha




