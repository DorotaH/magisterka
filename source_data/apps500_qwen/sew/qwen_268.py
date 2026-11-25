a, b = map(int, input().split())
if not a * b % 2 == 0:
    print("Odd")
else:
    print("Even")