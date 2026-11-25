MOD = 1000000007

def mod_inv(a, mod=MOD):
    return pow(a, mod - 2, mod)

def nCr(n, r, mod=MOD):
    if r > n:
        return 0
    num = den = 1
    for i in range(r):
        num = num * (n - i) % mod
        den = den * (i + 1) % mod
    return num * mod_inv(den, mod) % mod

def solve(n, f):
    if n < f:
        return 0
    if n == f:
        return 1
    ans = 0
    for i in range(1, f + 1):
        ans = (ans + nCr(n - 1, i - 1) * pow(i, n - i, mod)) % mod
    return ans

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    index = 1
    results = []
    for _ in range(q):
        n = int(data[index])
        f = int(data[index + 1])
        index += 2
        results.append(solve(n, f))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
