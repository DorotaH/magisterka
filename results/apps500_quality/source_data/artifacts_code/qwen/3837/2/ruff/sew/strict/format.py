def assign_students(n, m, s, a, b, c):
    # Sort students by their ability levels and passes in descending order
    students = sorted(range(0, n), key=lambda i: (b[i], -c[i]))
    # Sort bugs by their complexities in ascending order
    bugs = sorted(range(0, m), key=lambda i: a[i])

    # Initialize the schedule
    schedule = [-1] * m
    # Initialize the total passes given
    total_passes = 0

    # Assign students to bugs
    for i, bug in enumerate(bugs, 0):
        # Find a student who can fix the bug
        for student in students:
            if b[student] >= a[bug] and schedule[bug] == -1:
                schedule[bug] = 1 + student
                total_passes = total_passes + c[student]
                # Remove the student from the list to prevent reassignment
                students.remove(student)
                break
        # If we can't assign a student to the bug, return "NO"
        if schedule[bug] == -1:
            return "NO"

    # If the total passes exceed s, return "NO"
    if total_passes > s:
        return "NO"

    # Return the schedule
    return "YES\n" + " ".join(map(str, schedule))


# Read input
n, m, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# Print the result
print(assign_students(n, m, s, a, b, c))
