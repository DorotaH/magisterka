import sys

L = float(sys.stdin.readline())

volume = 0
max_volume = 0
for x in range(1, int(L) + 1):
	for y in range(x, int(L) + 1):
		for z in range(y, int(L) + 1):
			if y + x + z == L:
				volume = y * x * z
				max_volume = max(max_volume, volume)

print(round(max_volume, 7))
