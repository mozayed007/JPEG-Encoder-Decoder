import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.encoder.dct import Block8_DCT

def test_dct_zero_input():
    block = np.zeros((8, 8), dtype=np.uint8)
    dct_result = Block8_DCT(block)
    assert np.all(dct_result == 0)

def test_dct_constant_input():
    block = np.full((8, 8), 10, dtype=np.uint8)
    dct_result = Block8_DCT(block)
    try:
        assert dct_result[0, 0] != 0
        assert np.all(dct_result[0, 1:] == 0)
        assert np.all(dct_result[1:, :] == 0)
    except AssertionError:
        print(dct_result)
        raise
def test_dct_impulse_input():
    block = np.zeros((8, 8), dtype=np.uint8)
    block[0, 0] = 1
    dct_result = Block8_DCT(block)
    # Check that the output is a cosine wave
    for i in range(8):
        for j in range(8):
            assert np.isclose(dct_result[i, j], np.cos((2*i + 1) * j * np.pi / 16) * np.cos((2*j + 1) * i * np.pi / 16))
def test_dct():
    test_dct_zero_input()
    test_dct_constant_input()
    test_dct_impulse_input()

    # Create a 8x8 block of image data
    block = np.array([
        [52, 55, 61, 66, 70, 61, 64, 73],
        [63, 59, 55, 90, 109, 85, 69, 72],
        [62, 59, 68, 113, 144, 104, 66, 73],
        [63, 58, 71, 122, 154, 106, 70, 69],
        [67, 61, 68, 104, 126, 88, 68, 70],
        [79, 65, 60, 70, 77, 68, 58, 75],
        [85, 71, 64, 59, 55, 61, 65, 83],
        [87, 79, 69, 68, 65, 76, 78, 94]
    ], dtype=np.uint8)

    # Perform DCT
    dct_result = Block8_DCT(block)
    # Check the shape of the output
    assert dct_result.shape == block.shape

    # Check the type of the output
    assert isinstance(dct_result, np.ndarray)
