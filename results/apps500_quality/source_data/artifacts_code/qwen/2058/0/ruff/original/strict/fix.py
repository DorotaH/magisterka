def hamming_distance(a, b):
    return sum(abs(int(a[i]) - int(b[i])) for i in range(len(a)))

def sum_of_hamming_distances(a, b):
    n, m = len(a), len(b)
    total_distance = 0
    current_distance = hamming_distance(a, b[:n])
    total_distance += current_distance

    for i in range(n, m):
        current_distance += 2 * (int(b[i]) != int(b[i - n])) - (int(b[i - n]) != int(b[i - n + 1]))
        total_distance += current_distance

    return total_distance

# Read input
a = input().strip()
b = input().strip()

# Output the result
print(sum_of_hamming_distances(a, b))
