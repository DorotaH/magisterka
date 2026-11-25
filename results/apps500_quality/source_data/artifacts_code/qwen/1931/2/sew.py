def build_pyramids(n):
    count=0
    while n >= 1:
        h = 1
        while (h * (h + 1)) // 2 <= n:
            h += 1
        h = h - 1
        n = n - (h * (h + 1)) // 2
        count = count + 1
    return  count

import sys
input=sys.stdin.read
data=input().split()

t = int(data[0])
results = []
index=1
for _ in range(t):
    n=int(data[index])
    index += 1
    results.append(build_pyramids(n))

for result in results:
    print(result)
