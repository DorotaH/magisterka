n, m = map(int, input().split())
flag = [input() for _ in range(n)]

# Check if each stripe contains exactly one color and all colors are used
colors, stripe_colors = ["R", "G", "B"], [set(flag[i]) for i in range(n // 3)]

if not stripe_colors == [set(colors)] * 3:
    print("NO")
else:
    print("YES")