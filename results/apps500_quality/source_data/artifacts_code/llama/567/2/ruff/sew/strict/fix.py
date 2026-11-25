import sys


def  read_int():
    return  int(sys.stdin.readline())

def  read_ints():
    return  map(int, sys.stdin.readline().split())

def  read_str():
    return  sys.stdin.readline().strip()

def  read_strs():
    return  map(lambda  s: s.strip(), sys.stdin.readline().split())

def  solve():
    n = read_int()
    a = list(read_ints())

    if  n == 1:
        print(1)
        return None

    dp=[0]*(n + 1)
    dp[0]=0
    dp[1]=1
    for  i in  range(2, 1 + n):
        dp[i] = min(abs(a[i - 1] - 1) + dp[i - 1],
                    min(abs(a[i - 1] - 1) + dp[i - 2],
                        abs(10**6 - a[i - 1]) + dp[i - 2] if a[i - 1] > 10**5 else 10**5 * 2))

    print(dp[n])

if __name__=="__main__":
    solve()
