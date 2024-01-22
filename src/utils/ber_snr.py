import numpy as np
import matplotlib.pyplot as plt

def image_to_bit_sequence(image_path):
    """
    Convert an image file into a bit sequence.

    Args:
        image_path (str): The path to the image file.

    Returns:
        list: The bit sequence representing the image file.
    """
    with open(image_path, 'rb') as f:
        byte = f.read(1)
        bit_sequence = []

        while byte:
            # Convert each byte to its 8-bit binary representation
            bit_sequence.extend([int(bit) for bit in format(ord(byte), '08b')])
            byte = f.read(1)

    return bit_sequence

def calculate_ber(original_signal, decoded_signal):
    """
    Calculate the Bit Error Rate (BER) between the original and decoded signals.

    Args:
        original_signal (numpy.array): The original signal.
        decoded_signal (numpy.array): The decoded signal.

    Returns:
        float: The BER of the decoded signal.
    """
    # Calculate the number of bit errors
    bit_errors = np.sum(original_signal != decoded_signal)

    # Calculate the total number of bits
    total_bits = len(original_signal)

    # Calculate the BER
    ber = bit_errors / total_bits

    return ber

def calculate_snr(original_signal, noisy_signal):
    """
    Calculate the Signal-to-Noise Ratio (SNR) between the original and noisy signals.

    Args:
        original_signal (numpy.array): The original signal.
        noisy_signal (numpy.array): The noisy signal.

    Returns:
        float: The SNR of the noisy signal.
    """
    # Calculate the power of the original signal
    signal_power = np.mean(original_signal ** 2)

    # Calculate the power of the noise
    noise_power = np.mean((original_signal - noisy_signal) ** 2)

    # Calculate the SNR
    snr = 10 * np.log10(signal_power / noise_power)

    return snr

def plot_ber_vs_snr(ber_values, snr_values):
    """
    Plot the BER vs SNR curve.

    Args:
        ber_values (list): The list of BER values.
        snr_values (list): The list of SNR values.
    """
    plt.figure()
    plt.plot(snr_values, ber_values, 'o-')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.title('BER vs SNR')
    plt.show()