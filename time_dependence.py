import numpy as np
import matplotlib.pyplot as plt

def birth_rate(t, alpha, beta):
    # Define the time-dependent birth rate function
    return alpha * np.exp(-beta * t)

def gillespie_simulation(N0, t_end, dt, death_rate, alpha, beta):
    # Initialize the population size and time arrays
    N = np.zeros(int(t_end / dt) + 1)
    t = np.arange(0, t_end + dt, dt)
    N[0] = N0

    # Simulate the birth-death process
    for i in range(1, len(t)):
        birth_rate_i = birth_rate(t[i-1], alpha, beta)
        death_rate_i = death_rate
        total_rate = birth_rate_i + death_rate_i
        r1 = np.random.rand()
        tau = -np.log(r1) / total_rate
        if r1 < birth_rate_i / total_rate:
            N[i] = N[i-1] + 1
        else:
            N[i] = N[i-1] - 1

    return t, N

# Parameters
N0 = 10
t_end = 100
dt = 0.1
death_rate = 0.5
alpha = 2.0
beta = 0.1

# Run the simulation
t, N = gillespie_simulation(N0, t_end, dt, death_rate, alpha, beta)

# Plot the results
plt.plot(t, N)
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Birth-Death Process with Time-Dependent Birth Rate')
plt.show()