import numpy as np

def Block8_DCT(block_8):
    """
    Perform Discrete Cosine Transform (DCT) on an 8x8 block.

    Parameters:
    block_8 (numpy.ndarray): Input 8x8 block.

    Returns:
    numpy.ndarray: DCT result of the input block.
    """
    R, C = block_8.shape
    # initialize the basis block
    basis = np.zeros((R, C))
    if R != 8 or C != 8:
        print('Error in block size')
    # looping over the size of the basis and size of the input
    dct_result = np.zeros((8, 8))
    for u in range(8):
        for v in range(8):
            for x in range(8):
                for y in range(8):
                    # constructing the basis function
                    basis[x, y] = np.cos((1/16)*(2*x+1)*u*np.pi) * np.cos((1/16)*(2*y+1)*v*np.pi)
            dct_result[u, v] = np.sum(block_8 * basis)
            # dct_result[u, v] = np.sum(np.multiply(block_8 , basis))
    # Now Scaling
    dct_result[0, 0] = (1/64) * dct_result[0, 0]             # The first value in the block /64
    dct_result[0, 1:8] = (1/32) * dct_result[0, 1:8]         # The first row /32
    dct_result[1:8, 0] = (1/32) * dct_result[1:8, 0]         # The first column /32
    dct_result[1:8, 1:8] = (1/16) * dct_result[1:8, 1:8]     # the rest of the block/16
    return dct_result



# def Block8_DCT(block_8):
#     R, C = block_8.shape
#     if R != 8 or C != 8:
#         print('Error in block size')
#         return None

#     # Precompute the basis functions
#     x, y = np.meshgrid(range(8), range(8), indexing='ij')
#     u, v = x.copy(), y.copy()

#     # Compute the basis functions for all u, v, x, y at once
#     basis = np.cos((2*x + 1) * u * np.pi / 16) * np.cos((2*y + 1) * v * np.pi / 16)

#     # Apply the DCT formula
#     dct_result = np.sum(block_8.reshape(8, 8, 1, 1) * basis, axis=(0, 1))

#     # Scaling
#     alpha = np.ones((8,8))
#     alpha[0,0] = 1/2
#     alpha[0,1:] = 1/np.sqrt(2)
#     alpha[1:,0] = 1/np.sqrt(2)
#     dct_result *= alpha

#     return dct_result
