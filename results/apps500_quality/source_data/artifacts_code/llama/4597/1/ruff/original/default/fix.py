MOD = 10**9 + 7

def solve():
    n = int(input())
    power = 1
    factorial = 1

    for i in range(1, n+1):
        power = (power * i) % MOD
        factorial = (factorial * i) % MOD

    power = (power * pow(factorial, MOD - 2, MOD)) % MOD

    print(power)

if __name__ == "__main__":
    t = 1
    for _ in range(t):
        solve()
