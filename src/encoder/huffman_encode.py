import heapq
import collections


def huffman_encode(arr):
    """
    Huffman encodes an input array.

    Args:
        arr (list): The input array to be encoded.

    Returns:
        tuple: A tuple containing the encoded array and a dictionary mapping symbols to their Huffman codes.
    """
    # Flatten the input array and convert it to a list of tuples
    flat_arr = list(map(tuple, arr))

    # Count the frequency of each tuple in the list
    freq = collections.Counter(flat_arr)

    # Build the Huffman tree
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Flatten the Huffman tree and sort the nodes by symbol
    huff = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    # Create a dictionary that maps each symbol to its Huffman code
    huff_dict = {item[0]: item[1] for item in huff}

    # Use the dictionary to encode the input array
    encoded = [huff_dict[tuple(x)] for x in arr]

    return encoded, huff_dict