import numpy as np

def birth_death_transition_matrix(lambda_, mu, n, t):
    """
    Calculate the transition probability matrix of a birth-death process.

    Parameters:
    lambda_ (float): birth rate
    mu (float): death rate
    n (int): number of states
    t (float): time units

    Returns:
    P (numpy array): transition probability matrix
    """
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                P[i, j] = 1 - lambda_ * t - mu * t
            elif j == i + 1:
                P[i, j] = lambda_ * t
            elif j == i - 1:
                P[i, j] = mu * t
    return P

def calculate_probability(initial_state, final_state, lambda_, mu, n, t):
    """
    Calculate the probability that a birth-death process reaches a specific state
    after t time units, starting from an initial state.

    Parameters:
    initial_state (int): initial state
    final_state (int): final state
    lambda_ (float): birth rate
    mu (float): death rate
    n (int): number of states
    t (float): time units

    Returns:
    probability (float): probability of reaching the final state
    """
    P = birth_death_transition_matrix(lambda_, mu, n, t)
    initial_state_vector = np.zeros(n)
    initial_state_vector[initial_state] = 1
    final_state_vector = np.zeros(n)
    final_state_vector[final_state] = 1
    probability = np.dot(np.dot(initial_state_vector, P), final_state_vector)
    return probability

# Example usage:
lambda_ = 0.5  # birth rate
mu = 0.3  # death rate
n = 5  # number of states
t = 2.0  # time units
initial_state = 2
final_state = 3

probability = calculate_probability(initial_state, final_state, lambda_, mu, n, t)
print(f"The probability of reaching state {final_state} from state {initial_state} after {t} time units is {probability:.4f}")