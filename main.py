from train import  train_double_qLearning
from config import  EPSILON, GAMMA, ALPHA


def main():
    trained = train_double_qLearning(iterations=50, rows=5, cols=5, num_actions=4, alpha=ALPHA, gamma=GAMMA, epsilon=EPSILON)
    print(trained. Q_A, trained.Q_B)


if __name__ == "__main__":
    main()