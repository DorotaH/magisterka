import math

n, s = map(int, input().split())
total_happiness = 0
slices = [0] * (s + 1)
happy = [0] * (s + 1)

for _ in range(n):
    si, ai, bi = map(int, input().split())
    total_happiness += si * ai
    slices[si] += 1
    happy[si] += bi

pizza_count = math.ceil(n / 2)
total_pizzas = math.ceil(n / 2)
pizzas = math.ceil(n / 2)

for i in range(1, s + 1):
    if slices[i] >= 1:
        pizza_count = math.ceil(n / (i + 1))
        if pizza_count <= total_pizzas:
            total_pizzas = pizza_count
            for j in range(i + 1, s + 1):
                if slices[j] >= 1:
                    pizza_count = math.ceil(n / (i + j))
                    if pizza_count <= total_pizzas:
                        total_pizzas = pizza_count
                        break

for i in range(1, s + 1):
    if slices[i] >= 1:
        total_happiness += min(i * happy[i], (s * slices[i]))

print(total_happiness)
