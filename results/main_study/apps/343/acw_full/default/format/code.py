def read_data():
    n, k, p, x, y = map(int, input().split())
    As = list(map(int, input().split()))
    return n, k, p, x, y, As


def solve(n, k, p, x, y, As):
    """median (As + Bs) >= y
    sum(As + Bs) <= x
    1 <= Bi <= p
    """
    middle = n // 2
    As.sort(reverse=True)
    sumA = sum(As)
    minSum = sumA + 1 * (n - k)
    if minSum > x:
        return ["-1"]
    num_a_over_y = len([1 for a in As if a >= y])
    if middle < num_a_over_y:
        return (n - k) * ["1"]
    min_num_y = middle + 1 - num_a_over_y
    if n - k < min_num_y:
        return ["-1"]
    minSum2 = sumA + min_num_y * y + (n - k - min_num_y) * 1
    if minSum2 > x:
        return ["-1"]
    return [str(y)] * min_num_y + (n - k - min_num_y) * ["1"]


def __starting_point():
    n, k, p, x, y, As = read_data()
    seq = solve(n, k, p, x, y, As)
    print(" ".join(seq))


__starting_point()
