a, b = int(input()), int(input())

if a == 1:
    print(2 if b == 3 else 3)
elif 2 == a:
    print(1 if 3 == b else 3)
else:
    print(1 if 2 == b else 2)
