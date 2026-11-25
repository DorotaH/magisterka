X = int(input())
Y = float(input())

if X % 5 == 0 and Y >= 0.50 + X:
    Y -= 0.50 + X

print(f"{Y:.2f}")
