n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))

# Initialize the maximum height with the maximum height of the first student
max_height = max(h1[0], h2[0])

# Iterate through the students starting from the second student
for i in range(1, n):
	# Choose the student with the maximum height from the current row
	max_height += max(h1[i], h2[i])
# Print the maximum possible total height
print(max_height)
