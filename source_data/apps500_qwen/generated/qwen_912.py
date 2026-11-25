n, m = map(int, input().split())
flag = [input() for _ in range(n)]

# Check if each stripe contains exactly one color and all colors are used
colors = ['R', 'G', 'B']
stripe_colors = [set(flag[i]) for i in range(n // 3)]

if stripe_colors == [set(colors)] * 3:
    print("YES")
else:
    print("NO")
