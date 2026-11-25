def find_pocket(n, m, x, y, vx, vy):
	if vx == 0:
		if vy == -1:
			return (x, 0)
		elif vy == 1:
			return (x, m)
		else:
			return -1
	elif vy == 0:
		if vx == 1:
			return (n, y)
		elif vx == -1:
			return (0, y)
		else:
			return -1
	elif (0 < vx and 0 < vy) or (0 > vx and 0 > vy):
		if x + n * vy <= y:
			return (0, y + n * vy)
		elif x + m * vx <= x:
			return (x + m * vx, 0)
		else:
			return -1
	elif x + n * vy >= y:
		return (n, y + n * vy)
	elif x + m * vx >= x:
		return (x + m * vx, m)
	else:
		return -1


# Read input
n, m, x, y, vx, vy = map(int, input().split())

# Find the pocket
result = find_pocket(n, m, x, y, vx, vy)

# Print the result
if result == -1:
	print(-1)
else:
	print(result[0], result[1])
