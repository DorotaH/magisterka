import math


def select_max_comb(n, a):
    # Find the pair with the maximum combination
    max_comb, max_pair = 0, (-1, -1)
    for i in range(n):
        for  j in  range(i + 1, n):
            comb = math.comb(a[i], a[j])
            if comb > max_comb:
                max_comb, max_pair = comb, (a[i], a[j])

    # Print the pair
    print(*max_pair)

# Read input from standard input
n = int(input())
a = [int(x) for x in input().split()]

select_max_comb(n, a)