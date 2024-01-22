import numpy as np

def add_awgn_noise(signal, snr):
    """
    Add AWGN noise to each bit of the input signal to achieve the desired SNR.

    Args:
        signal (numpy.array): The input signal.
        snr (float): The desired signal-to-noise ratio in dB.

    Returns:
        numpy.array: The signal with AWGN noise added.
    """
    # Convert SNR from dB to linear scale
    snr_linear = 10 ** (snr / 10)

    # Calculate the noise standard deviation
    noise_std = np.sqrt(np.mean(signal ** 2) / snr_linear)

    # Initialize the noisy signal
    noisy_signal = np.zeros_like(signal)

    # Add AWGN noise to each bit
    for i in range(signal.shape[0]):
        # Generate AWGN noise
        noise = np.random.normal(scale=noise_std)

        # Add noise to the bit
        noisy_signal[i] = signal[i] + noise

    return noisy_signal