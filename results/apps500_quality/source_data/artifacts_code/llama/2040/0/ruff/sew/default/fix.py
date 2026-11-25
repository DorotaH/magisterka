
n = int(input())
b = [int(input()) for _ in range(n)]

a = list()
for i in range(n):
    a.append('')
    num=b[i]
    while num>0:
        a[i]=str(num%9)+a[i]
        num = num // 9

a = a[::-1]
a = a[1:] + ['1'] + a[0:-1]
a = list(map(int, a))
print(*a)