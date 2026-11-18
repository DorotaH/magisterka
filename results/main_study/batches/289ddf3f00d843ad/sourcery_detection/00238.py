def main():
	n = int(input())

	result = 0
	d = set()
	for _ in range(n):
		t, a = input().split()
		a = int(a)
		if t == "+":
			d.add(a)
			result = max(result, len(d))
		elif a in d:
			d.remove(a)
		else:
			result += 1

	print(result)


main()
