# This code shows a list of probabilities for each state from 0 to 100.
def stationary_distribution(lambda_val, mu_val, max_state=100):
    # Calculating
    beta = lambda_val / (lambda_val + mu_val)

    # Initializing
    dist = [0] * (max_state + 1)

    # first element of the distribution to (1 - beta)
    dist[0] = 1 - beta

    # Calculating the remaining elements of the distribution
    for i in range(1, max_state + 1):
        dist[i] = dist[i - 1] * beta

    return dist

# Examples to use
lambda_val = 0.5  # example of a birth rate
mu_val = 0.3  # example of a death rate

result = stationary_distribution(lambda_val, mu_val)
print(result)