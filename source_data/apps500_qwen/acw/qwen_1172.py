def max_segments(n, b, a, s):
	max_segments = 0
	current_battery = b
	current_accumulator = a

	for i in range(n):
		if s[i] == 1:
			if 0 < current_battery:
				current_battery -= 1
				current_accumulator += 1
				max_segments += 1
			elif 0 < current_accumulator:
				current_accumulator -= 1
				max_segments += 1
		elif 0 < current_battery:
			current_battery -= 1
			max_segments += 1
		elif 0 < current_accumulator:
			current_accumulator -= 1
			max_segments += 1
		else:
			break

	return max_segments


# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
b = int(data[1])
a = int(data[2])
s = list(map(int, data[3:]))

# Output the result
print(max_segments(n, b, a, s))
