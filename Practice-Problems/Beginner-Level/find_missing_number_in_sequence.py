# Problem: Find Missing Number in a Sequence
# You received log files indexed from 1 to n. One log is missing. Find it.

# Input: [1, 2, 4, 5]
# Output: 3

def find_missing_number_in_sequence(sequence):
    sequence_length = len(sequence)
    for i in range(0, sequence_length-1):
        if (sequence[i+1] - sequence[i]) > 1:
            return sequence[i+1] - 1
        
    return None

# output => 3
input = [1, 2, 4, 5]

# output => 6
input = [1, 2, 3, 4, 5, 7]

# output => None
# input = [1, 2, 3, 4, 5, 6, 7]
print("Input -> ", input)
print("Output -> ", find_missing_number_in_sequence(input))
