from collections import defaultdict


def f(x):
    """Dima's function f(x)"""
    if x == 0:
        return 0
    return f(x // 2) if x % 2 == 0 else 1 + f(x - 1)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)

    for num in a:
        cnt[f(num)] += 1

    ans = sum(count * (count - 1) // 2 for count in cnt.values())
    print(ans)


if __name__ == "__main__":
    main()
