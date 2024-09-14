import numpy as np

def birth_death_queue(lambda_birth, mu_death, initial_customers, time_steps):
    """
    Simulates a birth-death queueing system.

    Parameters:
    lambda_birth (float): birth rate (arrival rate)
    mu_death (float): death rate (service rate)
    initial_customers (int): initial number of customers
    time_steps (int): number of time steps to simulate

    Returns:
    customers_over_time (list): number of customers at each time step
    """
    customers_over_time = [initial_customers]
    for t in range(time_steps):
        # Calculate the number of arrivals and departures
        arrivals = np.random.poisson(lambda_birth)
        departures = np.random.poisson(mu_death * min(customers_over_time[-1], 1))
        
        # Update the number of customers
        new_customers = customers_over_time[-1] + arrivals - departures
        customers_over_time.append(new_customers)
    
    return customers_over_time

# Call the function with some input parameters
lambda_birth = 0.5
mu_death = 0.3
initial_customers = 10
time_steps = 100

# Simulate the birth-death queueing system
customers_over_time = birth_death_queue(lambda_birth, mu_death, initial_customers, time_steps)

# Print the result
print(customers_over_time)