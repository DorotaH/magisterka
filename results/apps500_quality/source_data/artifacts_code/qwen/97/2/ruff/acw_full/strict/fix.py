

def find_pocket(n, m, x, y, v_x, v_y):
	if v_x == 0 and v_y == 0:
		return -1

	# Normalize the direction vector
	if v_x == 0:
		return (0, m) if v_y > 0 else (0, 0)
	elif v_y == 0:
		return (n, 0) if v_x > 0 else (0, 0)
	elif v_x == v_y:
		return (n, m) if v_x > 0 else (0, 0)
	elif v_x == -v_y:
		return (n, 0) if v_x > 0 else (0, m)
	else:
		return -1


# Read input
n, m, x, y, v_x, v_y = map(int, input().split())

# Find and print the pocket
pocket = find_pocket(n, m, x, y, v_x, v_y)
print(pocket[0], pocket[1])
