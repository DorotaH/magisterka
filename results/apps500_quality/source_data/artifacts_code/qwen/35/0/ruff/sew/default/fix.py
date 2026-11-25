n, m = map(int, input().split())
flag = [input().strip() for _ in range(n)]

# Check if the flag has three equal stripes
stripes = [flag[i*n//3:(i+1)*n//3] for i in range(3)]

# Check if each stripe has exactly one color
for stripe in stripes:
    colors=set(stripe)
    if  1 != len(colors):
        print("NO")
        exit()

# Check if each color is used exactly once
colors = set()
for stripe in stripes:
    colors.update(stripe)
if len(colors) != 3:
    print("NO")
    exit()

print("YES")