class ConvolutionalEncoder:
    def __init__(self):
        self.state = [0, 0]  # Initial state is all zeros

    def encode_bit(self, bit):
        """
        Encodes a single bit using the convolutional encoding algorithm.

        Args:
            bit (int): The input bit to be encoded.

        Returns:
            list: The list of output bits after encoding the input bit.
        """
        # Update state
        self.state.insert(0, bit)
        self.state.pop()

        # Calculate output bits
        output_bits = [
            bit ^ self.state[0] ^ self.state[1],  # G1 = 1 + x + x^2
            bit ^ self.state[1],  # G2 = 1 + x^2
            bit ^ self.state[0]  # G3 = 1 + x
        ]

        return output_bits

    def encode(self, bits):
        """
        Encodes a sequence of bits using the convolutional encoding algorithm.

        Args:
            bits (list): The list of input bits to be encoded.

        Returns:
            list: The list of output bits after encoding the input bits.
        """
        encoded_bits = []

        for bit_string in bits:
            for bit in bit_string:
                # Convert the bit from string to int before encoding
                encoded_bits.extend(self.encode_bit(int(bit)))

            # Add zeros to return to all zeros state after each block
            for _ in range(2):
                encoded_bits.extend(self.encode_bit(0))

        return encoded_bits