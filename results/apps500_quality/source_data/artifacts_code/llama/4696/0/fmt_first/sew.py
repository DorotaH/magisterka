a, b = map(int, input().split())
product = b * a
if not product % 2 == 0:
    print("Odd")
else:
    print("Even")