import numpy as np

def dequantize(quantized_blocks, q_table):
    """
    Dequantizes the quantized blocks using the given quantization table.

    Args:
        quantized_blocks (list): List of quantized blocks.
        q_table (list): Quantization table.

    Returns:
        list: List of dequantized blocks.
    """
    # Multiply each block by the quantization table
    dequantized_blocks = [block * q_table for block in quantized_blocks]

    return dequantized_blocks