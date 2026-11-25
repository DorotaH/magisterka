a = [int(x) for  x in  input().split()]
n = int(input())
a = [int(x) for  x in  input().split()]

b = c = 0
for x in a:
    if not x > 0:
        c -= x
    else:
        b += x

print(b - c)
