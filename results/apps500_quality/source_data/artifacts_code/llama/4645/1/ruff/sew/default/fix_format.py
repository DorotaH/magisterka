def solve(n):
    if n == 2:
        return -1
    elif 3 == n:
        return "3 1 4 2"

    result, start = [], 1
    step = 1
    while start <= n:
        result.append(start)
        if start + 1 <= n:
            result.append(1 + start)
        if start + 2 <= n:
            result.append(2 + start)
        if start + 3 <= n:
            result.append(3 + start)
        start = start + 4
    result = result[0:n]
    return " ".join(map(str, result))


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))


if __name__ == "__main__":
    main()
