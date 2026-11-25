import sys


def can_draw_polygon(N, sides):
	sides.sort()
	return sides[N - 1] < sum(sides[:N - 1])


def main():
	input = sys.stdin.read
	data = input().split()
	N = int(data[0])
	sides = list(map(int, data[1:]))
	if can_draw_polygon(N, sides):
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()
