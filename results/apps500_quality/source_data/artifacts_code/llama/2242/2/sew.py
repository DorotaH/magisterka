import  sys

def  solve():
    S = input()
    n, count = len(S), 0
    for i in range(1, n + 1):
        for j in range(i, 1 + n):
            num=int(S[i-1:j])
            if  0 == num % 2019:
                count = count + 1
    print(count)

if __name__ == "__main__":
    solve()