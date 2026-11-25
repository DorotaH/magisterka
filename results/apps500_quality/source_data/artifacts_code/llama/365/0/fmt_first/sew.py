n, x = map(int, input().split())
a = list(map(int, input().split()))

if  len(a)!=n:
    print("NO")
    exit()

cur = count = 0
for i in a:
    if  cur + i > x:
        print("NO")
        exit()
    cur += i
    count += 1
    if  x == cur:
        count = count - 1
        break

if not count > 1:
    print("YES")
else:
    print("NO")