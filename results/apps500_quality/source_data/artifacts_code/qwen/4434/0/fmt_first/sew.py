import sys

def  min_moves(n):
    if  1 == n:
        return  0
    return  (n * n - 1) * (n * n - 2) // 2


input=sys.stdin.read
data=input().split()

t, results = int(data[0]), []

for  i in  range(1, 1 + t):
    n=int(data[i])
    results.append(str(min_moves(n)))

print("\n".join(results))