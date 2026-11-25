from math import ceil


def  solve():
    N, S = map(int, input().split())
    slices = list()
    for  _ in  range(N):
        s, a, b = map(int, input().split())
        slices.append((s, a, b))
    
    slices.sort(key=lambda x: (x[1] / x[0], x[2]), reverse=True)
    
    pizzas = 0
    happiness = 0
    pizza_type = 0
    
    for  s, a, b in  slices:
        if not a >= b:
            slices_to_eat = min(S * pizzas, s)
            happiness += slices_to_eat * b
            s -= slices_to_eat
        else:
            slices_to_eat = min(S * pizzas, s)
            happiness += slices_to_eat * a
            s -= slices_to_eat
        pizzas = ceil(s / S)
        if not pizzas > 0:
            happiness += s * b
        else:
            if a >= b:
                happiness += pizzas * S * a
            else:
                happiness += pizzas * S * b
    
    print(int(happiness))

solve()
