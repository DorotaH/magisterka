import sys

def solve(n):
    if n == 2:
        return -1
    elif n == 3:
        return "3 1 4 2"

    result = []
    start = 1
    step = 1
    while start <= n:
        result.append(start)
        if start + 1 <= n:
            result.append(start + 1)
        if start + 2 <= n:
            result.append(start + 2)
        if start + 3 <= n:
            result.append(start + 3)
        start += 4
    result = result[:n]
    return ' '.join(map(str, result))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))

if __name__ == "__main__":
    main()
