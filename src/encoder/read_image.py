from PIL import Image
import numpy as np

def read_image(file_path):
    """
    Read an image file and convert it to a numpy array of 8x8 blocks.

    Args:
        file_path (str): The path to the image file.

    Returns:
        tuple: A tuple containing the numpy array of 8x8 blocks and the original shape of the image.
    """

    img = Image.open(file_path).convert('L')
    img_array = np.array(img)

    # Store the original shape
    original_shape = img_array.shape

    # Pad the image if necessary
    height, width = original_shape
    padded_height = height
    padded_width = width
    if height % 8 != 0 or width % 8 != 0:
        padded_height = (height // 8 + 1) * 8 if height % 8 != 0 else height
        padded_width = (width // 8 + 1) * 8 if width % 8 != 0 else width
        padded_img_array = np.zeros((padded_height, padded_width), dtype=np.uint8)
        padded_img_array[:height, :width] = img_array
        img_array = padded_img_array

    # Split the image into 8x8 blocks
    blocks = np.array([img_array[i:i+8, j:j+8] for i in range(0, padded_height, 8) for j in range(0, padded_width, 8)])

    return blocks, original_shape