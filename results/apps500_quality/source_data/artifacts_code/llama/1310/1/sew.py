import  sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().split()))

max_xor = xor = 0
for i in range(0, 30):
    curr=1<<i
    for  j in  range(0, n):
        xor=curr^(a[j]^xor)
        max_xor=max(max_xor, xor)

print(max_xor)