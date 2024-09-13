def stationary_distribution(lambda_val, mu_val, max_state=100):
    # Calculate beta
    beta = lambda_val / (lambda_val + mu_val)

    # Initialize the stationary distribution list
    dist = [0] * (max_state + 1)

    # Set the first element of the distribution to (1 - beta)
    dist[0] = 1 - beta

    # Calculate the remaining elements of the distribution
    for i in range(1, max_state + 1):
        dist[i] = dist[i - 1] * beta

    return dist

# Example usage:
lambda_val = 0.5  # example birth rate
mu_val = 0.3  # example death rate

result = stationary_distribution(lambda_val, mu_val)
print(result)