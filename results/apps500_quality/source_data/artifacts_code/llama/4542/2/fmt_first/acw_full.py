s = input().strip()


def find_min_stones(s):
	n = len(s)
	black_count = s.count("B")
	white_count = n - black_count

	if black_count > white_count:
		return black_count - white_count
	else:
		return white_count - black_count


print(find_min_stones(s))
