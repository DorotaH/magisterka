import heapq

n, m, s = map(int, input().split())
bugs = list(map(int, input().split()))
students = []
students_cap = list(map(int, input().split()))
student_levels = list(map(int, input().split()))

# Create a list of students and their corresponding caps
students = [[student_levels[i], i, students_cap[i]] for i in range(n)]

# Sort the students by their levels in descending order
students.sort(reverse=True)

# Create a min-heap to store the bugs
bug_heap = []
for j in range(m):
    heapq.heappush(bug_heap, (bugs[j], j))

# Initialize variables to keep track of the number of passes and days
passes = 0
days = 0
assigned = [-1] * m

while bug_heap:
    # Get the student with the highest level
    student_level, student_index, _ = students.pop()

    # Get the bug with the lowest complexity
    bug_complexity, bug_index = heapq.heappop(bug_heap)

    # If the student's level is higher than or equal to the bug's complexity
    if bug_complexity <= student_level:
        # Assign the bug to the student
        assigned[bug_index] = student_index + 1

        # Increase the number of passes by the student's cap
        passes += students_cap[student_index]

        # Increase the number of days
        days += 1

        # If the student's cap is 0, break the loop
        if students_cap[student_index] == 0:
            break
    else:
        # If the student's level is lower than the bug's complexity, push the bug back into the heap
        heapq.heappush(bug_heap, (bug_complexity, bug_index))

# If the number of passes exceeds the university's capabilities
if passes > s:
    print("NO")
else:
    print("YES")
    print(' '.join(map(str, assigned)))
