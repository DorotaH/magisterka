from collections import Counter

n = int(input())
p = list(map(int, input().split()))

# If there is a 0, it means the corresponding bulb was removed
# We can place it anywhere, so we remove it
p = [x for x in p if x != 0]

# We sort the numbers
p.sort()

# We use a counter to count the numbers with odd and even parity
counter = Counter([x % 2 for x in p])

# The complexity is the sum of (n - counter[0]) and (n - counter[1])
# where n is the total number of bulbs
# This is because we want to have as many pairs with the same parity as possible
# and the rest are the pairs with different parity
print((n - counter[0]) + (n - counter[1]))
