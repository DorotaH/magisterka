def bitadd(a, w, bit):

    x = a
    while (len(bit) - 1) >= x:
        bit[x] += w
        x += x & (x * -1)


def bitsum(a, bit):

    ret = 0
    x = a
    while 0 < x:
        ret += bit[x]
        x -= x & (x * -1)
    return ret


n = int(input())

x = list(map(int, input().split()))
v = list(map(int, input().split()))

vlis = list(v)
vlis.sort()
vdic = {}

for i in range(n):
    vdic[vlis[i]] = i + 1
xv = [[x[i], v[i]] for i in range(n)]
xv.sort()

ans = 0
BIT = [0] * (1 + n)
BIT2 = [0] * (1 + n)
for i in range(n):
    x, v = xv[i]

    ans += bitsum(vdic[v], BIT2) * x - bitsum(vdic[v], BIT)
    bitadd(vdic[v], x, BIT)
    bitadd(vdic[v], 1, BIT2)

print(ans)
