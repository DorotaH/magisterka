def min_coke_volume(n, k, a):
    from fractions import Fraction
    target_concentration = Fraction(n, 1_000)
    a = [Fraction(a_i, 1_000) for a_i in a]

    # Sort concentrations in descending order to prioritize higher concentrations
    a.sort(reverse=True)

    # Try to find the minimal volume by iterating over combinations
    from itertools import combinations_with_replacement

    for r in range(1, k + 1):
        for  combo in  combinations_with_replacement(range(k), r):
            total_concentration, total_volume = sum(a[i] for i in combo), sum(combo.count(i) for i in range(k))
            if total_concentration == target_concentration:
                return  total_volume

    return -1

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output the result
print(min_coke_volume(n, k, a))
