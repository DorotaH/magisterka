import heapq
from collections import defaultdict


def assign_bugs(n, m, s, a, b, c):
	# Dictionary to store the number of passes each student wants to get
	passes_needed = defaultdict(int)
	for i in range(n):
		passes_needed[i] = c[i]

	# List of available students sorted by their ability levels
	available_students = []
	for i in range(n):
		heapq.heappush(available_students, (b[i], i))

	# List to store the assignment of bugs to students
	assignment = [-1] * m

	# Total number of passes given
	total_passes = 0

	# Iterate over each bug
	for j in range(m):
		# Get the most suitable student for the current bug
		while available_students and available_students[0][0] < a[j]:
			heapq.heappop(available_students)

		if not available_students:
			return "NO"

		# Assign the bug to the most suitable student
		student = heapq.heappop(available_students)
		assignment[j] = student[1]
		total_passes += 1

		# Decrease the passes needed for the assigned student
		passes_needed[student[1]] -= 1
		if passes_needed[student[1]] == 0:
			heapq.heappush(available_students, (b[student[1]], student[1]))

	# Check if the total passes given is within the limit
	if total_passes > s:
		return "NO"

	return "YES\n" + " ".join(map(str, assignment + [0] * (n - m)))


# Read input
n, m, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Output the result
print(assign_bugs(n, m, s, a, b, c))
