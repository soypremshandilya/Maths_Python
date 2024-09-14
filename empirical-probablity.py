import numpy as np
import matplotlib.pyplot as plt

def birth_death_process(lambda_birth, lambda_death, initial_population, max_time, num_runs):
    """
    Simulate multiple runs of a birth-death process and compute the empirical probability distribution of the population size.

    Parameters:
    lambda_birth (float): birth rate
    lambda_death (float): death rate
    initial_population (int): initial population size
    max_time (float): maximum time to simulate
    num_runs (int): number of runs to simulate

    Returns:
    population_sizes (list of lists): list of population sizes at each time step for each run
    empirical_distribution (dict): empirical probability distribution of the population size
    """
    population_sizes = []
    for _ in range(num_runs):
        population = [initial_population]
        time = 0
        while time < max_time:
            birth_rate = lambda_birth * population[-1]
            death_rate = lambda_death * population[-1]
            rate = birth_rate + death_rate
            dt = np.random.exponential(scale=1/rate)
            time += dt
            if np.random.rand() < birth_rate / rate:
                population.append(population[-1] + 1)
            else:
                population.append(population[-1] - 1)
        population_sizes.append(population)

    empirical_distribution = {}
    for population in population_sizes:
        for size in population:
            if size not in empirical_distribution:
                empirical_distribution[size] = 0
            empirical_distribution[size] += 1
    for size in empirical_distribution:
        empirical_distribution[size] /= num_runs * max_time

    print("Empirical distribution:", empirical_distribution)

    return population_sizes, empirical_distribution

# Example usage:
lambda_birth = 0.5
lambda_death = 0.3
initial_population = 10
max_time = 100
num_runs = 1000

population_sizes, empirical_distribution = birth_death_process(lambda_birth, lambda_death, initial_population, max_time, num_runs)

print("Plotting empirical distribution...")
plt.bar(list(empirical_distribution.keys()), list(empirical_distribution.values()))
plt.xlabel('Population Size')
plt.ylabel('Empirical Probability')
plt.title('Empirical Probability Distribution of Population Size')
plt.show()