

def assign_bugs_to_students(n: int, m: int, s: int, a: list[int], b: list[int], c: list[int]) -> list[int]:
    # Sort students by their ability levels and bugs by their complexities
    students, bugs = sorted([(b[i], i) for i in range(n)], reverse=True), sorted([(a[i], i) for i in range(m)])
    
    # Initialize the schedule and passes given to each student
    schedule, passes_given = [-1] * m, [0] * n
    
    # Try to assign bugs to students
    for bug_complexity, bug_index in bugs:
        for student_ability, student_index in students:
            if  bug_complexity <= student_ability and  1 + passes_given[student_index]<=c[student_index]:
                schedule[bug_index]=student_index + 1
                passes_given[student_index]+=1
                break
        else:
            # If we can't assign this bug to any student, return "NO"
            return "NO"
    
    # Check if the total passes given do not exceed the limit
    if  sum(passes_given) > s:
        return "NO"
    
    return "YES\n"+" ".join(map(str, schedule))

# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n, m = int(data[0]), int(data[1])
s, a = int(data[2]), list(map(int, data[3:3+m]))
b, c = list(map(int, data[3+m:3+m+n])), list(map(int, data[3+m+n:]))

# Get the result and print it
result = assign_bugs_to_students(n, m, s, a, b, c)
print(result)