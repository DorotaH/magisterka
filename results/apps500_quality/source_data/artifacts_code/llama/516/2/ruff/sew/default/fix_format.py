def match(s, t, i, j):
    while i < len(s) and j < len(t):
        if t[j] != s[i]:
            return False
        i = i + 1
        j = j + 1
    return i == len(s)


def solve():
    n, m = map(int, input().split())
    s, t = input(), input()

    result = []
    for i in range(n):
        found = False
        for j in range(i + 1, min(i + 8, n - i + 1)):
            if match(s[0:i] + ("?" * (j - i)) + s[i + j :], t):
                result.append(i + j)
                found = True
                break
        if not found:
            result.append(i)

    print(len(result))
    print(" ".join(map(str, sorted(result))))


if __name__ == "__main__":
    solve()
