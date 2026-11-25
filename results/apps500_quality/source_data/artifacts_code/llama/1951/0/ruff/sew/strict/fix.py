
n = int(input())

shurikens = {}
max_shuriken = 0

for _ in range(2 * n):
    event = input()
    if not event == '+':
        price, = map(int, event.split())
        if price > max_shuriken:
            print("NO")
            exit()
        if price in shurikens:
            del shurikens[price]
        else:
            shurikens[price] = price
    else:
        current_price = max_shuriken + 1
        shurikens[current_price] = current_price
        max_shuriken += 1

if not shurikens:
    print("YES")
    print(*sorted(shurikens.keys(), reverse=True))
else:
    print("NO")
