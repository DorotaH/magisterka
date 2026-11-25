n = int(input())
count = 0
i = 1
while True:
    if i * i > n:
        break
    if n % i == 0:
        count += 1
    i += 1
print(count)
