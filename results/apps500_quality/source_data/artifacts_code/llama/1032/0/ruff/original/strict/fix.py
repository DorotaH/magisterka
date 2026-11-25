from math import gcd


def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def read_strs():
    return input().split()

def read_ints_minus_one():
    return map(lambda x: int(x) - 1, input().split())

MOD = 10 ** 9 + 7

def main():
    n, p = read_ints()
    a = list(read_ints())

    def totient(x):
        ans = x
        for i in range(1, n + 1):
            if x % i == 0:
                ans -= ans // i
        return ans

    s = sum(a)
    ans = 0
    good = []
    for x in range(1, s + 1):
        if gcd(x, p) == 1:
            if totient(x) != 0 and totient(x) % p != 0:
                ans += 1
                good.append(x)
    print(ans)
    for i in good:
        print(i, end=' ')
    print()

if __name__ == "__main__":
    main()
