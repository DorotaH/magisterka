
n, a, x, b, y = map(int, input().split())


def get_position(station, start, end):
    if start <= end:
        return (start - 1) % n + 1, (end - 1) % n + 1
    else:
        return (start - 1) % n + 1, (end + n - 1) % n + 1


a_pos, x_pos = get_position(a, a, x)
b_pos, y_pos = get_position(n - b + 1, n - b + 1, y - 1)

max_pos = max(max(a_pos, x_pos), max(b_pos, y_pos))

for i in range(max_pos):
    if (a_pos + i) % n == (i + b_pos) % n:
        print("YES")
        break
else:
    print("NO")
