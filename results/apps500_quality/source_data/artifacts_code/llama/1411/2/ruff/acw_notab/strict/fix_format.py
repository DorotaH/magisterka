from math import ceil


def solve():
    N, S = map(int, input().split())
    slices = []
    for _ in range(N):
        s, a, b = map(int, input().split())
        slices.append((s, a, b))

    slices.sort(key=lambda x: (x[1] / x[0], x[2]), reverse=True)

    pizzas = 0
    happiness = 0
    pizza_type = 0

    for s, a, b in slices:
        slices_to_eat = min(pizzas * S, s)
        happiness += a * slices_to_eat if a >= b else b * slices_to_eat
        s -= slices_to_eat
        pizzas = ceil(s / S)
        if pizzas > 0:
            happiness += pizzas * S * a if a >= b else pizzas * S * b
        else:
            happiness += b * s

    print(int(happiness))


solve()
