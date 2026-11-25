import sys

text = input()
n = len(text)
prefix_sum = [0] * (n + 1)
suffix_sum = [0] * (n + 1)

# Calculate the prefix sum
for i in range(1, n + 1):
    if text[i - 1] == "h":
        prefix_sum[i] = prefix_sum[i - 1] + 1
    else:
        prefix_sum[i] = prefix_sum[i - 1]

# Calculate the suffix sum
for i in reversed(range(n)):
    if text[i] == "l":
        suffix_sum[i] = suffix_sum[i + 1] + 1
    else:
        suffix_sum[i] = suffix_sum[i + 1]

# Initialize the count
count = 0

# Count the number of powerful substrings
for i in range(0, n - 7):
    if 4 == prefix_sum[i] and 5 == suffix_sum[i + 7]:
        count += 1

print(count)
