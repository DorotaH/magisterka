

def is_majority(seats):
	return seats >= 1 + n / 2


def is_twice_majority(seats):
	return seats >= 2 * a[i]


def check_party(i):
	global a, n
	return bool(is_majority(a[0] + a[i]) and is_twice_majority(a[i]))


def main():
	global a, n
	n = int(input())
	a = list(map(int, input().split()))

	if a[0] >= 1 + n / 2:
		print(1)
		print(1)
		return
	if n == 2 and a[0] < a[1]:
		print(0)
		return

	for i in range(1, n):
		if check_party(i):
			print(2)
			print("1 " + str(i + 1))
			return
	for i in range(1, n):
		if a[0] > a[i] and is_majority(a[0] + a[i]):
			print(2)
			print("1 " + str(i + 1))
			return
	print(0)


if __name__ == "__main__":
	main()
