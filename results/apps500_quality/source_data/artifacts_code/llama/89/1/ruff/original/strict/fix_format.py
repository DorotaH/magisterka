n = int(input())

layers = 0
current_end = 0
for i in range(n + 1):
    current_end = i
    if (current_end + (n - current_end) + 1) > (n - current_end) * 2:
        layers += 1
        current_end = n

print(layers)
