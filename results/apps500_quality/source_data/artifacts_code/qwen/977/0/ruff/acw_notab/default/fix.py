def count_good_integers(n, p, a):
    from itertools import permutations
    
    def is_valid_permutation(perm, a):
        yuzu_candies = perm[0]
        for i in range(1, n):
            if a[perm[i]] <= yuzu_candies:
                yuzu_candies += 1
            else:
                return False
        return True
    
    good_integers = []
    for x in range(1, 1 + n):
        valid_permutations = 0
        for perm in permutations(range(1, 1 + n)):
            if perm[0] == x and is_valid_permutation(perm, a):
                valid_permutations += 1
        if valid_permutations % p != 0:
            good_integers.append(x)
    
    return len(good_integers), good_integers


# Read input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Get the result
result = count_good_integers(n, p, a)

# Print the result
print(result[0])
print(*result[1])
