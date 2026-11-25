
def read_int():
    return int(input())

def read_ints():
    return list(map(int, input().split()))

def read_string():
    return input().strip()

def read_strings():
    return input().split()

MOD = 10 ** 9 + 7

def solve():
    n, a = read_int(), read_ints()
    a.sort()
    a=[0]+a
    ans=0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if abs(a[i]-a[j])<=abs(a[i]+a[j]):
                ans = ans + 1
    print(ans)

if  __name__ == "__main__":
    t = 1
    for  _ in  range(t):
        solve()