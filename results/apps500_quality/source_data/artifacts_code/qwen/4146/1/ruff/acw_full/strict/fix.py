import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
v = list(map(int, data[1:]))

# Count occurrences of each number
from collections import Counter

count = Counter(v)

# Find the two most common numbers
most_common = count.most_common(2)
num1, count1 = most_common[0]
num2, count2 = most_common[1]

# Calculate the minimum number of replacements needed
# If the two most common numbers are the same, we need to change all elements to the other number
# Otherwise, we need to change all elements that are not the most common numbers
min_replacements = n if num1 == num2 else n - max(count1, count2)
print(min_replacements)
