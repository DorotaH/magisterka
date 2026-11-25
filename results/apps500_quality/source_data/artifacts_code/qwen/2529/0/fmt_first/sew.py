X, Y = int(input()), float(input())

if  X % 5 == 0 and  Y>=X + 0.50:
    Y-=X + 0.50

print(f"{Y:.2f}")