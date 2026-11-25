x, a, b = map(int, input().split())
if not abs(x - a) < abs(x - b):
    print('B')
else:
    print('A')
