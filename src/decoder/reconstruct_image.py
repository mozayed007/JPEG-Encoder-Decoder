import numpy as np

def reconstruct_image(blocks, original_shape, block_size=8):
    """
    Reconstructs the image from the given blocks.

    Args:
        blocks (list): List of image blocks.
        original_shape (tuple): Original shape of the image.
        block_size (int, optional): Size of each block. Defaults to 8.

    Returns:
        numpy.ndarray: Reconstructed image array.
    """
    # Calculate the padded shape
    padded_height = (original_shape[0] // block_size + 1) * block_size if original_shape[0] % block_size != 0 else original_shape[0]
    padded_width = (original_shape[1] // block_size + 1) * block_size if original_shape[1] % block_size != 0 else original_shape[1]

    # Reshape the blocks into the padded shape
    img_array = np.block([[blocks[i * padded_width // block_size + j] for j in range(padded_width // block_size)] for i in range(padded_height // block_size)])

    # Crop the image to the original shape
    img_array = img_array[:original_shape[0], :original_shape[1]]

    return img_array