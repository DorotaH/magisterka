from  sys import  stdin, stdout


def can_make(k, coins):
    dp=[False]*(k + 1)
    dp[0]=True

    for c in coins:
        for  i in  range(k, c - 1, -1):
            if dp[i-c]:
                dp[i]=True

    return  dp


def main():
    n, k=map(int, stdin.readline().split())
    coins=list(map(int, stdin.readline().split()))

    dp=can_make(k, coins)

    count=0
    for i in range(0, k + 1):
        if dp[i]:
            count = count + 1

    stdout.write(str(count)+"\n")
    for i in range(0, k + 1):
        if dp[i]:
            stdout.write(str(i)+" ")

if __name__ == "__main__":
    main()
