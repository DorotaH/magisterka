def find_string(t):
	n = len(t)
	for k in range(1, 1 + n):
		if n % k == 0:
			s = t[:k] * (n // k)
			if all(t[i] in s[i:i + len(t)] for i in range(len(t))):
				return s


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	T = int(data[0])
	results = []
	index = 1
	for _ in range(T):
		t = data[index]
		index += 1
		results.append(find_string(t))
	for result in results:
		print(result)


if __name__ == "__main__":
	main()
