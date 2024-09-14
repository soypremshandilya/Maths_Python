import numpy as np

def expected_individuals(birth_rate, death_rate, initial_population, time):
    """
    Calculate the expected number of individuals at a given time in a birth-death process.

    Parameters:
    birth_rate (float): The rate at which individuals are born.
    death_rate (float): The rate at which individuals die.
    initial_population (int): The initial number of individuals.
    time (float): The time at which to calculate the expected number of individuals.

    Returns:
    float: The expected number of individuals at the given time.
    """
    lambda_ = birth_rate
    mu = death_rate
    N0 = initial_population
    t = time

    # Calculate the expected number of individuals using the formula:
    # E[N(t)] = N0 * (lambda_ / (lambda_ + mu)) * (1 - (mu / lambda_) * exp(-t * (lambda_ + mu)))
    expected_N = N0 * (lambda_ / (lambda_ + mu)) * (1 - (mu / lambda_) * np.exp(-t * (lambda_ + mu)))

    return expected_N

birth_rate = 0.5
death_rate = 0.2
initial_population = 10
time = 5

expected_N = expected_individuals(birth_rate, death_rate, initial_population, time)
print("The expected number of individuals at time t={} is: {}".format(time, expected_N))