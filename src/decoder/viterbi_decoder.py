class ViterbiDecoder:
    def __init__(self):
        self.state_metric = [0, float('inf'), float('inf'), float('inf')]
        self.state_history = []

    def hard_decision(self, bit):
        return 1 if bit > 0 else 0

    def decode_bit(self, bits):
        next_state_metric = [float('inf')] * 4
        next_state_history = [(0, 0)] * 4

        for current_state in range(4):
            for input_bit in [0, 1]:
                # Calculate next state and output bits
                next_state = ((current_state << 1) | input_bit) & 3
                output_bits = [
                    input_bit ^ (current_state & 1) ^ ((current_state >> 1) & 1),  # G1 = 1 + x + x^2
                    input_bit ^ ((current_state >> 1) & 1),  # G2 = 1 + x^2
                    input_bit ^ (current_state & 1)  # G3 = 1 + x
                ]

                # Calculate metric for this path
                path_metric = sum(self.hard_decision(bit) != output_bit for bit, output_bit in zip(bits, output_bits))

                # Update state metric and history if this path is better
                total_metric = self.state_metric[current_state] + path_metric
                if total_metric < next_state_metric[next_state]:
                    next_state_metric[next_state] = total_metric
                    next_state_history[next_state] = (current_state, input_bit)

        self.state_metric = next_state_metric
        self.state_history.append(next_state_history)

    def decode(self, bits):
        # Apply hard decision demodulation
        bits = [self.hard_decision(bit) for bit in bits]

        # Decode bits in groups of 3
        for i in range(0, len(bits), 3):
            self.decode_bit(bits[i:i+3])

        # Trace back through state history to find most likely path
        decoded_bits = []
        current_state = 0  # End in all zeros state
        for state_history in reversed(self.state_history):
            current_state, bit = state_history[current_state]
            decoded_bits.append(bit)

        return list(reversed(decoded_bits[:-2]))  # Remove added zeros