def find_kth_digit(k):
	number = 1
	while True:
		num_str = str(number)
		if len(num_str) >= k:
			return int(num_str[k - 1])
		k -= len(num_str)
		number += 1


# Read input
k = int(input())

# Output the result
print(find_kth_digit(k))
