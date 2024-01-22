import numpy as np

def run_length_encode(input):
    """
    Run-length encodes an input array.

    Parameters:
    input (ndarray): The input array to be encoded.

    Returns:
    ndarray: The run-length encoded array.

    """
    # Find the indices where the value changes
    indices = np.where(np.diff(input) != 0)[0] + 1

    # Use these indices to split the input into runs
    runs = np.split(input, indices)

    # For each run, take the first value and the length
    output = np.array([(run[0], len(run)) for run in runs])

    return output

