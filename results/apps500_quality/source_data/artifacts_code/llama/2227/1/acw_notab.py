import sys

text = input()
n = len(text)
prefix_sum = [0] * (1 + n)
suffix_sum = [0] * (1 + n)

# Calculate the prefix sum
for i in range(1, 1 + n):
    if text[i - 1] == 'h':
        prefix_sum[i] = prefix_sum[i - 1] + 1
    else:
        prefix_sum[i] = prefix_sum[i - 1]

# Calculate the suffix sum
for i in range(n - 1, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + 1 if text[i] == 'l' else suffix_sum[i + 1]
# Initialize the count
count = 0

# Count the number of powerful substrings
for i in range(n - 7):
    if prefix_sum[i] == 4 and suffix_sum[i + 7] == 5:
        count += 1

print(count)
