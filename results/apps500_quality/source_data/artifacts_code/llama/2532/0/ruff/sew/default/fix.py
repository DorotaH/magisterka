import sys


def  solve():
    p, q = map(int, sys.stdin.readline().split())
    a, b = list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))
    d, X = list(map(int, sys.stdin.readline().split())), list(map(int, sys.stdin.readline().split()))

    n, m = len(X), 10**6

    for  i in  range(1, 1+p):
        a[i] %= m
    for  i in  range(1, 1+q):
        d[i] %= m

    def find_coefficients(a, b, p, q):
        A = []
        for i in range(1, 1+p):
            A.append(a[i])

        for i in range(1, 1+q):
            A.append(b[i])

        return A

    A, B = find_coefficients(a, b, p, q), [0] * (n+1)

    for  i in  range(n):
        B[1+i] = (sum(X[i-j+1] * A[j] for  j in  range(min(i+1, p+1))) + sum(d[k] * pow(10, k, m) for k in range(min(i+1, q+1))) % m) % m

    for  i in  range(10):
        print(B[n + i], end=' ')

def  main():
    T = 1
    for  _ in  range(T):
        solve()

if  __name__ == '__main__':
    main()