from  sys import  stdin, stdout

# Read input
n, k = map(int, stdin.readline().split())
coins = list(map(int, stdin.readline().split()))

# Initialize a set to store all possible sums that can be made with a subset of coins
possible_sums = set([0])

# Iterate over each coin and update the possible sums
for coin in coins:
    new_sums=possible_sums.copy()
    for  s in  possible_sums:
        if  s+coin<=k:
            new_sums.add(s+coin)
    possible_sums.update(new_sums)

# Find all possible sums that can be made with a subset of coins that pays for the chocolate
result = [x for x in range(k + 1) if x in possible_sums]

# Write output
stdout.write(f"{len(result)}\n")
stdout.write(" ".join(map(str, result)))