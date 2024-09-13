import numpy as np
import matplotlib.pyplot as plt

def birth_death_process(birth_rate, death_rate, initial_population, time_steps):
    population = np.zeros(time_steps)
    population[0] = initial_population
    
    for i in range(1, time_steps):
        birth_events = np.random.poisson(np.clip(birth_rate * population[i-1], 0, 1000))
        death_events = np.random.poisson(np.clip(death_rate * population[i-1], 0, 1000))
        population[i] = population[i-1] + birth_events - death_events
    
    return population

def plot_population(population, time_steps):
    plt.plot(np.arange(time_steps), population, label='Population Size')
    plt.xlabel('Time Steps')
    plt.ylabel('Population Size')
    plt.title('Birth-Death Process Simulation')
    plt.legend()
    plt.show()

# parameters
birth_rate = 0.5
death_rate = 0.3
initial_population = 100
time_steps = 100

# Running simulation
population = birth_death_process(birth_rate, death_rate, initial_population, time_steps)

# Plotting
plot_population(population, time_steps)