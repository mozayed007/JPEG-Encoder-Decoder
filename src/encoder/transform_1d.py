import numpy as np

def serpentine_scan(quantized_mat):
    """
    Perform serpentine scan on a quantized matrix.

    Args:
        quantized_mat (numpy.ndarray): The quantized matrix.

    Returns:
        numpy.ndarray: The scanned array.
    """
    n, m = 8, 8  # dimensions of the block
    x, y = 0, 0  # starting indices
    scanned_array = np.zeros(n*m, dtype=float)  # output array

    for i in range(n*m):
        scanned_array[i] = quantized_mat[x, y]  # add current element to the output array

        # update indices
        if ((x + y) % 2 == 0):  # moving up
            if y < m-1 and x > 0:
                x -= 1
                y += 1
            elif y < m-1:
                y += 1
            elif x < n-1:
                x += 1
        else:  # moving down
            if x < n-1 and y > 0:
                x += 1
                y -= 1
            elif x < n-1:
                x += 1
            elif y < m-1:
                y += 1

    return scanned_array