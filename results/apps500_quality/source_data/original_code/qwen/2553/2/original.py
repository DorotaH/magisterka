import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    x = int(data[index + 1])
    a = list(map(int, data[index + 2:index + 2 + n]))
    index += 2 + n
    
    # Count the number of odd numbers in the array
    odd_count = sum(1 for num in a if num % 2 != 0)
    
    # Check if it's possible to select x elements such that their sum is odd
    if odd_count >= x:
        results.append("Yes")
    else:
        results.append("No")

# Print all results
for result in results:
    print(result)
