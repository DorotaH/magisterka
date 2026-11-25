n = int(input())

layers = current_end = 0
for i in range(n + 1):
    current_end = i
    if  (current_end + (n - current_end) + 1) > 2 * (n - current_end):
        layers = layers + 1
        current_end=n

print(layers)
