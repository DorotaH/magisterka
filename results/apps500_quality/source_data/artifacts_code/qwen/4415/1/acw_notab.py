def split_sequences(n, a):
    if n == 1:
        return "YES\n0\n\n0\n"

    increasing = []
    decreasing = []
    i = 0

    while i < n:
        if i == 0 or a[i - 1] < a[i]:
            increasing.append(a[i])
            i += 1
        elif a[i - 1] > a[i]:
            decreasing.append(a[i])
            i += 1
        else:
            return "NO"

    if not increasing or not decreasing:
        return "NO"

    return f"YES\n{len(increasing)}\n{' '.join(map(str, increasing))}\n{len(decreasing)}\n{' '.join(map(str, decreasing))}\n"


# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Print output
print(split_sequences(n, a))
