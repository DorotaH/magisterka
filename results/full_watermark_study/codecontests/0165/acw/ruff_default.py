z = [1]
z.extend(2 * z[-1] for _ in range(30))
for i in range(int(input())):
    l, r = list(map(int, input().split()))
    x = r // 2 - (l - 1) // 2
    for i in range(31):
        cr = (r // (2 * z[i])) * z[i]
        if r % (2 * z[i]) >= z[i]:
            cr += r % (2 * z[i]) - z[i] + 1
        cl = ((l - 1) // (2 * z[i])) * z[i]
        if (l - 1) % (2 * z[i]) >= z[i]:
            cl += (l - 1) % (2 * z[i]) - z[i] + 1
        x = min(x, r - l + 1 - cr + cl)
    print(x)
