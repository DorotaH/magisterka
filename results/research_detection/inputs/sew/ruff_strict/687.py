def recur_gcd(a, b):
    low, high = min(a, b), max(a, b)
    if low == 0:
        return high
    if low == 1:
        return 1
    return recur_gcd(low, high % low)
