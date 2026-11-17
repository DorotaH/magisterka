from sys import stdin, gettrace

if gettrace():
    def inputi():
        return input()
else:
    def input():
        return next(stdin)[:-1]


    def inputi():
        return stdin.buffer.readline()

LIMIT = 200001
MOD = 1000000007

def solve(factorial):
    n = int(input())
    print( (factorial[2*n]*pow(2, MOD-2, MOD))%MOD)

def main():
    factorial = [1]
    factorial.extend((factorial[-1]*i)%MOD for i in range(1, LIMIT))
    t = int(input())
    for _ in range(t):
        solve(factorial)


if __name__ == "__main__":
    main()
