import numpy as np

def Block8_IDCT(block_8):
    """
    Perform inverse discrete cosine transform (IDCT) on an 8x8 block.

    Args:
        block_8 (numpy.ndarray): Input 8x8 block.

    Returns:
        numpy.ndarray: Resulting 8x8 block after IDCT.
    """
    R, C = block_8.shape
    # Initializations
    basis = np.zeros((R, C))
    if R != 8 or C != 8:
        print('Error in block size')
    # looping over the size of the basis and size of the input
    idct_result = np.zeros((8, 8))
    for u in range(8):
        for v in range(8):
            for x in range(8):
                for y in range(8):
                    # constructing the basis block
                    basis[x, y] = np.cos((1/16)*(2*x+1)*u*np.pi) * np.cos((1/16)*(2*y+1)*v*np.pi)
            # multiplying each value of encoded_block to the corresponding
            # basis block and summing the result and storing it in the result_Idct block
            idct_result += block_8[u, v] * basis
    return idct_result

# def Block8_IDCT(dct_result):
#     R, C = dct_result.shape
#     if R != 8 or C != 8:
#         print('Error in block size')
#         return None

#     # Precompute the basis functions
#     u, v = np.meshgrid(range(8), range(8), indexing='ij')
#     x, y = u.copy(), v.copy()

#     # Compute the basis functions for all u, v, x, y at once
#     basis = np.cos((2*x + 1) * u * np.pi / 16) * np.cos((2*y + 1) * v * np.pi / 16)

#     # Apply the IDCT formula
#     idct_result = np.sum(dct_result.reshape(8, 8, 1, 1) * basis, axis=(2, 3))

#     # Scaling
#     alpha = np.ones((8,8))
#     alpha[0,0] = 1/2
#     alpha[0,1:] = 1/np.sqrt(2)
#     alpha[1:,0] = 1/np.sqrt(2)
#     idct_result *= alpha

#     return idct_result