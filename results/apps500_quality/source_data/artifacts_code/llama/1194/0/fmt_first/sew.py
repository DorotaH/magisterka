import  sys
import  math


def read_ints():
    return  list(map(int, input().split()))


def main():
    n, p = int(input()), read_ints()
    q=read_ints()

    p, q = [n - 1 - i for i in range(n)], [n - 1 - i for i in range(n)]

    a=[0]*n
    for  i in  range(0, n):
        a[p[i]] = q[i]

    print(*a)


if __name__=="__main__":
    main()
