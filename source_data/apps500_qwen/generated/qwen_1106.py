def can_select_elements(n, x, a):
    # Count the number of odd elements in the array
    odd_count = sum(1 for num in a if num % 2 != 0)
    
    # To get an odd sum, we need either:
    # 1. An odd number of odd elements (if x is odd)
    # 2. An even number of odd elements (if x is even)
    if x % 2 == 1:
        return odd_count >= x
    else:
        return odd_count <= x

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process each test case
t = int(data[0])
index = 1
results = []
for _ in range(t):
    n = int(data[index])
    x = int(data[index + 1])
    a = list(map(int, data[index + 2:index + 2 + n]))
    index += 2 + n
    results.append("Yes" if can_select_elements(n, x, a) else "No")

# Print results
print('\n'.join(results))
