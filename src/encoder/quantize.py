import numpy as np

def QuantizationTable(x):
    """
    Returns the quantization table based on the input value of x.

    Parameters:
    x (str): The value to determine the type of quantization table. Should be either 'low' or 'high'.

    Returns:
    np.array: The quantization table as a NumPy array.

    Raises:
    ValueError: If the input value of x is not 'low' or 'high'.
    """
    if x == 'low':
        Table = [[1, 1, 1, 1, 1, 2, 2, 4],
                    [1, 1, 1, 1, 1, 2, 2, 4],
                    [1, 1, 1, 1, 2, 2, 2, 4],
                    [1, 1, 1, 1, 2, 2, 4, 8],
                    [1, 1, 2, 2, 2, 2, 4, 8],
                    [2, 2, 2, 2, 2, 4, 8, 8],
                    [2, 2, 2, 4, 4, 8, 8, 16],
                    [4, 4, 4, 4, 8, 8, 16, 16]]
    elif x == 'high':
        Table = [[1, 2, 4, 8, 16, 32, 64, 128],
                    [2, 4, 4, 8, 16, 32, 64, 128],
                    [4, 4, 8, 16, 32, 64, 128, 128],
                    [8, 8, 16, 32, 64, 128, 128, 256],
                    [16, 16, 32, 64, 128, 128, 256, 256],
                    [32, 32, 64, 128, 128, 256, 256, 256],
                    [64, 64, 128, 128, 256, 256, 256, 256],
                    [128, 128, 128, 256, 256, 256, 256, 256]]
    else:
        raise ValueError('Invalid value for x. Expected low or high.')
    return np.array(Table)

def quantize(dct_blocks, quality):
    """
    Quantizes the given DCT blocks using the specified quality.

    Args:
        dct_blocks (list): List of DCT blocks.
        quality (int): Quality factor for quantization.

    Returns:
        numpy.ndarray: Quantized DCT blocks.
    """
    # Get the quantization table
    q_table = QuantizationTable(quality)

    # Perform the quantization step per 8x8 block
    q_blocks = np.array([block / q_table for block in dct_blocks])

    return q_blocks