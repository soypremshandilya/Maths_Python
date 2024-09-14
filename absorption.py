import numpy as np

def compute_expected_time(Q, absorbing_states):
    """
    Compute the expected time until absorption in a birth-death process.

    Parameters:
    Q (numpy array): Transition rate matrix
    absorbing_states (list): List of absorbing states

    Returns:
    expected_time (numpy array): Expected time until absorption for each state
    """
    num_states = Q.shape[0]
    absorbing_states = np.array(absorbing_states)

    # Create a matrix to store the expected times
    expected_time = np.zeros(num_states)

    # Iterate over each state
    for i in range(num_states):
        # If the state is absorbing, the expected time is 0
        if i in absorbing_states:
            expected_time[i] = 0
        else:
            # Compute the expected time using the formula:
            # E[T] = 1 / (sum of rates out of state i) + sum of (rate from i to j) * E[T_j]
            rates_out = Q[i, :]
            rates_out[i] = 0  # exclude the rate from i to itself
            expected_time_i = 1 / np.sum(rates_out)
            for j in range(num_states):
                if j != i:
                    expected_time_i += Q[i, j] * expected_time[j]
            expected_time[i] = expected_time_i

    return expected_time

# Example usage:
Q = np.array([
    [-2, 1, 1, 0],
    [1, -3, 1, 1],
    [0, 1, -2, 1],
    [0, 0, 1, -1]
])  # Transition rate matrix
absorbing_states = [3]  # List of absorbing states

expected_time = compute_expected_time(Q, absorbing_states)
print("Expected time until absorption:", expected_time)