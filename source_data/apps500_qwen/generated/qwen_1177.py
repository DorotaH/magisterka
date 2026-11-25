import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
v = list(map(int, data[1:]))

# Count the occurrences of each number
count = {}
for num in v:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# Find the two most frequent numbers
max1 = max2 = 0
num1 = num2 = 0
for num, cnt in count.items():
    if cnt > max1:
        max2 = max1
        num2 = num1
        max1 = cnt
        num1 = num
    elif cnt > max2:
        max2 = cnt
        num2 = num

# Calculate the minimum number of replacements needed
replacements = n - 2 * max1 - max2

# If there are more than two different numbers, we need to replace at least one more
if len(count) > 2:
    replacements += 1

print(replacements)
