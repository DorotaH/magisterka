def is_lucky(n):
	"""Check if a number is lucky."""
	return "8" in str(abs(n))


def find_lucky_floor(n):
	"""Find the minimum positive integer b such that n + b is a lucky floor number."""
	if is_lucky(n):
		return 0
	n = abs(n)
	while True:
		n += 1
		if is_lucky(n):
			return n - abs(n)


def main():
	n = int(input())
	print(find_lucky_floor(n))


if __name__ == "__main__":
	main()
