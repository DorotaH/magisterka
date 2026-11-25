n = int(input())
b = [int(input()) for _ in range(n)]

a = []
prev = 0
for i in b:
    prev += 1
    k=0
    while i>0:
        k=i % 10+10 * k
        i = i // 10
    a.append(k+prev)

print('\n'.join(map(str, a)))
