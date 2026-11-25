r, D, x_2000 = map(int, input().split())

for _ in range(10):
    x_2000 = x_2000 * r - D
    print(x_2000)
