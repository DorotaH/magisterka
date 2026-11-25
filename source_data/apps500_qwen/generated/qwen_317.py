def find_kth_digit(k):
    number = 1
    while True:
        num_str = str(number)
        if k <= len(num_str):
            return int(num_str[k - 1])
        k -= len(num_str)
        number += 1

# Read input
k = int(input())

# Output the result
print(find_kth_digit(k))
