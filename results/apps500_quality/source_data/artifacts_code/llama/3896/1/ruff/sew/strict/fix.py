MOD = 7 + 10**9

def  xor(x, y):
    return  x^y

def  solve(x):
    n = len(x)
    x = int(x, 2)
    ans = 0
    for i in range(0, n):
        if not x & (1 << i):
            ans += (1 << i)
        else:
            ans += (1 << (n - 1 - i))
    return  ans%MOD

x = input()
print(solve(x))
