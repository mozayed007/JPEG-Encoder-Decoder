from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import log10, sqrt
import os

def calculate_compression_ratio(original_file_path, compressed_file_path):
    """
    Calculates the compression ratio between an original file and a compressed file.

    Parameters:
    original_file_path (str): The path to the original file.
    compressed_file_path (str): The path to the compressed file.

    Returns:
    float: The compression ratio, which is the minimum value between the original file size divided by the compressed file size and the compressed file size divided by the original file size.
    """
    original_file_size = os.path.getsize(original_file_path)
    compressed_file_size = os.path.getsize(compressed_file_path)
    # Ensure the compression ratio is always less than or equal to 1
    return min(original_file_size / compressed_file_size, compressed_file_size / original_file_size)

def compare_images(original_image, compressed_image, original_file_path, compressed_file_path, title):
    """
    Compare two images by calculating the Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR),
    and compression ratio between them.

    Parameters:
    - original_image: The original image.
    - compressed_image: The compressed image.
    - original_file_path: The file path of the original image.
    - compressed_file_path: The file path of the compressed image.
    - title: The title of the compressed image.

    Returns:
    - title: The title of the compressed image.
    - mse: The Mean Squared Error between the images.
    - psnr: The Peak Signal-to-Noise Ratio.
    - compression_ratio: The compression ratio.
    """
    # Convert images to numpy arrays
    original_image_array = np.array(original_image)
    compressed_image_array = np.array(compressed_image)
    
    # Convert images to grayscale if they have more than 2 dimensions
    if original_image_array.ndim > 2:
        original_image_array = np.mean(original_image_array, axis=-1)
    if compressed_image_array.ndim > 2:
        compressed_image_array = np.mean(compressed_image_array, axis=-1)
    
    # Crop the images to the same size
    min_shape = min(original_image_array.shape, compressed_image_array.shape)
    original_image_array = original_image_array[:min_shape[0], :min_shape[1]]
    compressed_image_array = compressed_image_array[:min_shape[0], :min_shape[1]]

    # Calculate Mean Squared Error between the two images
    mse = mean_squared_error(original_image_array, compressed_image_array)

    # Calculate PSNR
    if(mse == 0):   # MSE is zero means no noise is present in the signal .
                    # Therefore PSNR have no importance.
        psnr = 100
    else:
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))

    # Calculate the compression ratio
    compression_ratio = calculate_compression_ratio(original_file_path, compressed_file_path)

    # Display the original image
    plt.figure(figsize=(10, 5))
    plt.imshow(original_image_array, cmap='gray')
    plt.title('Original Image')
    plt.show()

    # Display the compressed image
    plt.figure(figsize=(10, 5))
    plt.imshow(compressed_image_array, cmap='gray')
    plt.title(title)
    plt.show()

    # Print the Mean Squared Error, PSNR, and compression ratio
    print(f'Mean Squared Error between the images: {mse}')
    print(f'Peak Signal-to-Noise Ratio: {psnr}')
    print(f'Compression Ratio: {compression_ratio}')
    # Return the results
    return title, mse, psnr, compression_ratio