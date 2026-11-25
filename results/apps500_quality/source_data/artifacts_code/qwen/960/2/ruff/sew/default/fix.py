n, k = map(int, input().split())

# Initialize the smallest x to a large number
smallest_x = float('inf')

# Iterate through possible values of x
for x in range(1, 10**7):
    if  (x // k) * (x % k) == n:
        smallest_x=min(smallest_x, x)
        break  # Since we are looking for the smallest x, we can break once we find it

print(smallest_x)