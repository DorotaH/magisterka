n, eggs = int(input()), []
for  _ in  range(n):
    a, g = map(int, input().split())
    eggs.append((a, g))

eggs.sort(key=lambda  x: x[0])

total_a = total_g = 0
diff = 0
result, a_count = '', 0
g_count = 0
for  a, g in  eggs:
    if diff <= 500 and diff + g - a <= 500:
        total_a += a
        result += 'A'
        a_count = a_count + 1
    elif diff >= -500 and diff + a - g >= -500:
        total_g += g
        result += 'G'
        g_count = g_count + 1
    else:
        diff = g - a
        result += 'G'
        g_count = g_count + 1
        total_g += g

    if abs(total_a - total_g) > 500:
        print(-1)
        exit()

print(result)
