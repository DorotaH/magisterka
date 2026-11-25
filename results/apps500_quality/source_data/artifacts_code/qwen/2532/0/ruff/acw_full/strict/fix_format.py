from sys import stdin, stdout

# Read input
p, q = map(int, stdin.readline().split())
coeffs = [int(stdin.readline()) for _ in range(p)]
coeffs.extend(int(stdin.readline()) for _ in range(q))
sequence = list(map(int, stdin.readline().split()))

# Function to calculate the next value in the sequence


def next_value(seq, coeffs):
    n = len(seq)
    a = sum(coeffs[i] * seq[n - 1 - i] for i in range(p))
    b = sum(coeffs[q + p - 1 - i] * i**n for i in range(1, q + 1))
    return (a + b) % 1000000


# Calculate the next 10 values
result = [next_value(sequence, coeffs) for _ in range(10)]

# Output the result
stdout.write(" ".join(map(str, result)) + "\n")
