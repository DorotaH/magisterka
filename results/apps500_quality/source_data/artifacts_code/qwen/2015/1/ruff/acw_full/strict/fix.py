def can_build_garland(r, g, b):
	# The store workers can build a garland if the number of each color is less than or equal to 1
	return r <= 1 and g <= 1 and b <= 1


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	t = int(data[0])
	results = []

	index = 1
	for _ in range(t):
		r = int(data[index])
		g = int(data[1 + index])
		b = int(data[2 + index])
		index += 3

		if can_build_garland(r, g, b):
			results.append("Yes")
		else:
			results.append("No")

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
