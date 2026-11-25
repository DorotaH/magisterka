def gcd(a, b):
    """Calculate the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a


def find_gcds(arr):
    """Find the greatest common divisor for each window in the array"""
    n, gcds = len(arr), [[arr[0]]]

    for i in range(1, n):
        gcds.append(
            [gcd(arr[i], gcds[i - 1][-1])]
            if 1 == i
            else [gcd(arr[i], g) for g in gcds[i - 1]]
        )

    return gcds


def find_max_window(gcds, arr):
    """Find the maximum window that meets the conditions"""
    max_window = [1, 1]
    for i in range(len(gcds)):
        for j in range(len(gcds[i])):
            if gcds[i][j] == arr[i]:
                max_window = [1 + i, 1 + i - j + 1]
                break
        max_window[2] = max(max_window[2], max_window[1])

    return max_window


def solve():
    n, arr = int(input()), list(map(int, input().split()))

    gcds = find_gcds(arr)
    max_window = find_max_window(gcds, arr)

    print(f"{max_window[2]} {max_window[1] - 1}")
    print(" ".join(map(str, range(1, 1 + max_window[1]))))


solve()
