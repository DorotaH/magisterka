def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_sequence_in_table(n, m, k, sequence):
    for i in range(1, n + 1):
        current_gcd = gcd(i, 1)
        for j in range(2, m + 1):
            current_gcd = gcd(current_gcd, j)
            if current_gcd == sequence[0]:
                found = True
                for l in range(1, k):
                    if gcd(i, j + l) != sequence[l]:
                        found = False
                        break
                if found:
                    return "YES"
    return "NO"


# Read input
n, m, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Print output
print(find_sequence_in_table(n, m, k, sequence))
