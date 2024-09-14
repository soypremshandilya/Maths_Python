import numpy as np
import matplotlib.pyplot as plt

def birth_death_process(n, birth_rate, death_rate):
    """
    Compute the stationary distribution of a birth-death process.

    Parameters:
    n (int): The number of states in the process.
    birth_rate (float): The rate at which births occur.
    death_rate (float): The rate at which deaths occur.

    Returns:
    pi (array): The stationary distribution of the process.
    """
    pi = np.zeros(n)
    pi[0] = 1
    for i in range(1, n):
        pi[i] = pi[i-1] * birth_rate / death_rate
    pi /= np.sum(pi)
    return pi

def visualize_stationary_distribution(pi):
    """
    Visualize the stationary distribution of a birth-death process using a bar chart.

    Parameters:
    pi (array): The stationary distribution of the process.
    """
    plt.bar(range(len(pi)), pi)
    plt.xlabel('State')
    plt.ylabel('Probability')
    plt.title('Stationary Distribution of Birth-Death Process')
    plt.show()

# Example usage:
n = 10
birth_rate = 0.5
death_rate = 0.3
pi = birth_death_process(n, birth_rate, death_rate)
visualize_stationary_distribution(pi)