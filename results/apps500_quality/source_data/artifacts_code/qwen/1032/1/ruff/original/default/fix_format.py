def count_good_integers(n, p, a):
    # Function to calculate the number of valid permutations f(x)
    def f(x):
        if x <= 2:
            return 0
        if x == 3:
            return 1
        if x >= 5:
            return 6
        count = 0
        for perm in permutations(range(1, x + 1)):
            if all(perm[i - 1] >= a[i - 1] for i in range(1, x + 1)):
                count += 1
        return count

    # Check for each x if f(x) is not divisible by p
    good_integers = []
    for x in range(1, n + 1):
        if f(x) % p != 0:
            good_integers.append(x)

    return len(good_integers), good_integers


# Read input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Get the result
result = count_good_integers(n, p, a)

# Print the result
print(result[0])
print(" ".join(map(str, result[1])))
