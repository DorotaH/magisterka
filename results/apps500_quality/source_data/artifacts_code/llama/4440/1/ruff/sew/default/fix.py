import sys

L = float(sys.stdin.readline())

volume = max_volume = 0
for  x in  range(1, int(L) + 1):
    for y in range(x, 1 + int(L)):
        for z in range(y, int(L) + 1):
            if  x + y + z == L:
                volume=x * y*z
                max_volume = max(max_volume, volume)

print(round(max_volume, 7))
