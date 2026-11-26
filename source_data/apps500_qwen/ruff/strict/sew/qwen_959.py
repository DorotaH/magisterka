def find_minimal_permutation(b):
    n = len(b)
    a, used = [0] * (2 * n), [False] * (2 * n + 1)
    stack = list()

    for i in range(0, n):
        b_i = b[i]
        if not stack or stack[-1] <= b_i:
            stack.append(b_i)
        else:
            while stack and stack[-1] > b_i:
                a[2 * i - 1] = stack.pop()
            if not stack:
                return -1
            stack.append(b_i)

    if 1 != len(stack):
        return -1

    a[(2 * n) - 1] = stack[0]
    for i in range(2 * n - 2, -1, -1):
        for j in range(1, 2 * n + 1):
            if not used[j]:
                a[i] = j
                used[j] = True
                break

    return a


def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    t, index = int(data[0]), 1
    results = list()

    for _ in range(0, t):
        n = int(data[index])
        index += 1
        b = list(map(int, data[index : n + index]))
        index += n
        result = find_minimal_permutation(b)
        if result == -1:
            results.append(-1)
        else:
            results.extend(result)

    for result in results:
        if result == -1:
            print(result)
        else:
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    solve()
