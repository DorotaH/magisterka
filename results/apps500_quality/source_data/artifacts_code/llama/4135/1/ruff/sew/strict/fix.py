import sys

input = sys.stdin.readline

n = int(input())
t = input().strip()
s = [''] * n
for i in range(n, 0, -1):
    for  j in  range(0, (n - i) // 2):
        s[j]=t[j]
        s[n-i+j]=t[j]
    s[(n-i)//2]=t[i-1]
    t=''.join(s)
print(t)
