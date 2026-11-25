import sys


def main():
	input_lines = sys.stdin.read().strip().split('\n')
	t = int(input_lines[0])
	for i in range(1, t + 1):
		n = int(input_lines[i])
		print((1 + n) % 2)


if __name__ == "__main__":
	main()
