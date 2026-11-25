import sys


def can_draw_polygon():
	N = int(input())
	lengths = list(map(int, input().split()))

	longest_side = max(lengths)
	other_sides_sum = sum(lengths[:-1])  # sum of all sides except the longest

	return 'Yes' if longest_side < other_sides_sum else 'No'


if __name__ == "__main__":
	sys.stdout.write(can_draw_polygon())
