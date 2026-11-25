import math

x = int(input())

min_ops = float('inf')

for i in range(1, 5):
	for j in range(1, 5):
		if (i + j) == 7:
			total = 0
			ops = 0
			for k in range(1, 5):
				for l in range(1, 5):
					if (l + k) == 7:
						total += 7 if k == i and l == j else l
						ops += 1
			if x <= total:
				min_ops = min(min_ops, ops)

print(min_ops)
