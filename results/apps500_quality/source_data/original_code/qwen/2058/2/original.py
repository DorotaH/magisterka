def hamming_distance(a, b):
    return sum(abs(int(a[i]) - int(b[i])) for i in range(len(a)))

def solve(a, b):
    n = len(a)
    m = len(b)
    total_distance = 0
    
    for i in range(m - n + 1):
        substring = b[i:i + n]
        total_distance += hamming_distance(a, substring)
    
    return total_distance

# Read input
a = input().strip()
b = input().strip()

# Solve and print the result
print(solve(a, b))
