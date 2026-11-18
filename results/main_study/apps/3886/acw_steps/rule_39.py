f0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
ft1, ft2, ft3 = 'What are you doing while sending "', '"? Are you busy? Will you send "', '"?'

flen = [2 * 10 ** 18] * (1 + 10 ** 5)
flen[0] = len(f0)
for i in range(1, 56):
    flen[i] = len(ft2) + len(ft1) + len(ft3) + 2 * flen[i-1]

def ans(n, k):
    while True:
        if n == 0:
            return f0[k]
        if k < len(ft1):
            return ft1[k]
        k -= len(ft1)
        if flen[n-1] > k:
            n -= 1
            continue
        k -= flen[n-1]
        if len(ft2) > k:
            return ft2[k]
        k -= len(ft2)
        if flen[n-1] > k:
            n -= 1
            continue
        k -= flen[n-1]
        return ft3[k]

q = int(input())
a = ''
for _ in range(q):
    n, k = list(map(int, input().split()))
    k -= 1
    if flen[n] <= k:
        a += '.'
        continue
    a += ans(n, k)
print(a)
