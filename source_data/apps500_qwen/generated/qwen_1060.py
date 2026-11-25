def min_fret_difference(strings, notes):
    # Create a list of tuples (note, string_index)
    pairs = [(note, i) for i, strings in enumerate(strings) for note in range(strings, strings + 1000)]
    pairs.sort(key=lambda x: x[0])
    
    # Initialize variables
    min_fret = float('inf')
    max_fret = float('-inf')
    used_frets = set()
    
    # Iterate through the sorted pairs to find the minimal difference
    for note, string_index in pairs:
        if note not in used_frets:
            used_frets.add(note)
            min_fret = min(min_fret, note)
            max_fret = max(max_fret, note)
        if len(used_frets) == len(strings):
            break
    
    return max_fret - min_fret

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse input
strings = list(map(int, data[0].split()))
n = int(data[1])
notes = list(map(int, data[2:]))

# Get the result
result = min_fret_difference(strings, notes)

# Print the result
print(result)
