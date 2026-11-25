n = int(input())
h = list(map(int, input().split()))
a = [0] * n
max_height = 0
for i in range(n-1, -1, -1):
    if not h[i] > max_height:
        a[i] = max_height - h[i]
    else:
        max_height = h[i]
print(' '.join(map(str, a)))
