def restore_string(s1, s2, s3):
	n = len(s1)
	for i in range(n):
		for j in range(i + 1, n):
			s1 = swap(s1, i, j)
			s2 = swap(s2, i, j)
			s3 = swap(s3, i, j)
			if s1 == s2 == s3:
				return s1
			s1 = swap(s1, i, j)
			s2 = swap(s2, i, j)
			s3 = swap(s3, i, j)
	return -1


def swap(s, i, j):
	return s[j] + s[:i] + s[i + 1:j] + s[i] + s[1 + j:]


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	k = int(data[0])
	n = int(data[1])
	strings = [data[i + 2] for i in range(k)]
	for i in range(k):
		strings[i] = strings[i][:n]
	result = restore_string(strings[0], strings[1], strings[2])
	if result == -1:
		print(result)
	else:
		print(result[:n])


if __name__ == "__main__":
	main()
