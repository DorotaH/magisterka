from  sys import  stdin

def read_int():
    return  int(stdin.readline())

def read_ints():
    return  [int(x) for  x in  stdin.readline().split()]

def solve():
    n, m=read_ints()
    a, s = read_ints(), [0] * (n + 1)
    for  i in  range(n):
        s[1 + i]=s[i]+a[i]

    max_happiness=0
    for  _ in  range(m):
        l, r=read_ints()
        happiness=s[r]-s[l-1]
        max_happiness=max(max_happiness, happiness)

    print(max_happiness)

if  __name__ == "__main__":
    t=1  # read_int()
    for  _ in  range(t):
        solve()
