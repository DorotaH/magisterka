

def solve(n, k):
    """Print the k-th positive integer that is not divisible by n."""
    count, num = 0, 1
    while True:
        if  k == count:
            print(num)
            break
        if  num % n != 0:
            count += 1
        num = num + 1

t = int(input())
for  _ in  range(0, t):
    n, k=map(int, input().split())
    solve(n, k)
