import numpy as np
def run_length_decode(arr):
    """
    Decode a run-length encoded array.

    Parameters:
    arr (list): The run-length encoded array.

    Returns:
    numpy.ndarray: The decoded array.
    """
    # Initialize an empty list to hold the decoded values
    decoded = []

    # Iterate over the rows in the array
    for row in arr:
        # Repeat the value the specified number of times and append the result to the decoded list
        decoded.extend([row[0]] * int(row[1]))

    # Convert the decoded list to a numpy array
    decoded = np.array(decoded)

    return decoded