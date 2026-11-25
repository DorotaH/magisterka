import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
results = []

index = 1
for _ in range(t):
    n = int(data[index])
    k = int(data[1 + index])
    index += 2
    
    # The k-th number not divisible by n is k + (k // (n - 1))
    # This is because for every n numbers, (n // (n - 1)) numbers are divisible by n
    result = (k // (n - 1)) + k
    results.append(result)

# Print all results
for result in results:
    print(result)
