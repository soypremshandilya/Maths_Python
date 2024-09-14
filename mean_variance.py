def calculate_mean_and_variance(birth_rate, death_rate):
    """
    Calculate the mean and variance of the population size at steady state
    in a birth-death process.

    Parameters:
    birth_rate (float): The rate at which individuals are born
    death_rate (float): The rate at which individuals die

    Returns:
    mean (float): The mean population size at steady state
    variance (float): The variance of the population size at steady state
    """
    mean = birth_rate / death_rate
    variance = birth_rate / (death_rate ** 2)
    return mean, variance

# Example usage:
birth_rate = 0.5  # Birth rate (e.g., 0.5 individuals per unit time)
death_rate = 0.3  # Death rate (e.g., 0.3 individuals per unit time)

mean, variance = calculate_mean_and_variance(birth_rate, death_rate)
print(f"Mean: {mean:.4f}")
print(f"Variance: {variance:.4f}")