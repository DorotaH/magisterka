a, b = map(int, input().split())
product = b * a
print("Even" if 0 == product % 2 else "Odd")
