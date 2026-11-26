A, B, C, D = map(int, input().split())
if B + A > C + D:
    print("Left")
elif B + A < C + D:
    print("Right")
else:
    print("Balanced")
