

def assign_bugs_to_students(n: int, m: int, s: int, a: list[int], b: list[int], c: list[int]) -> list[int]:
	# Sort students by their ability levels and bugs by their complexities
	students = sorted([(b[i], i) for i in range(n)], reverse=True)
	bugs = sorted([(a[i], i) for i in range(m)])
	
	# Initialize the schedule and passes given to each student
	schedule = [-1] * m
	passes_given = [0] * n
	
	# Try to assign bugs to students
	for bug_complexity, bug_index in bugs:
		for student_ability, student_index in students:
			if bug_complexity <= student_ability and 1 + passes_given[student_index] <= c[student_index]:
				schedule[bug_index] = student_index + 1
				passes_given[student_index] += 1
				break
		else:
			# If we can't assign this bug to any student, return "NO"
			return "NO"
	
	# Check if the total passes given do not exceed the limit
	if sum(passes_given) > s:
		return "NO"
	
	return "YES\n" + " ".join(map(str, schedule))


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
s = int(data[2])
a = list(map(int, data[3:m + 3]))
b = list(map(int, data[m + 3:m + 3 + n]))
c = list(map(int, data[m + 3 + n:]))

# Get the result and print it
result = assign_bugs_to_students(n, m, s, a, b, c)
print(result)
