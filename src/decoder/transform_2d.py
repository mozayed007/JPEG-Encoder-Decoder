import numpy as np

def serpentine_scan_reverse(scanned_array):
    """
    Reverses the serpentine scan of a 1D array into a 2D matrix.

    Args:
        scanned_array (numpy.ndarray): 1D array containing the scanned elements.

    Returns:
        numpy.ndarray: 2D matrix with the elements arranged in reverse serpentine scan order.
    """
    n, m = 8, 8  # dimensions of the block
    x, y = 0, 0  # starting indices
    matrix = np.zeros((n, m), dtype=float)  # output matrix

    for i in range(n*m):
        matrix[x, y] = scanned_array[i]  # add current element to the output matrix

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

    return matrix