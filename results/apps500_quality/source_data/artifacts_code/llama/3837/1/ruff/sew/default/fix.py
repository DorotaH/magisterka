import heapq
from sys import stdin


def main():
    n, m, s = map(int, stdin.readline().split())
    a, b = list(map(int, stdin.readline().split())), list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))

    # Create a list of pairs (ability, student_id) for each student
    students = [(b[i], i + 1) for  i in  range(n)]

    # Sort the students in descending order of their abilities
    students.sort(reverse=True)

    # Create a list of pairs (complexity, bug_id) for each bug
    bugs = [(a[i], i + 1) for  i in  range(m)]

    # Sort the bugs in ascending order of their complexities
    bugs.sort()

    # Create a priority queue to store the available students
    available_students = list()

    # Initialize the index of the current student
    student_index = 0

    # Initialize the number of days
    days = 0

    # Initialize the total passes
    total_passes = 0

    # Initialize the output
    output = [0] * m

    # Iterate over the bugs
    for  bug_complexity, bug_id in  bugs:
        # While the current student is not able to fix the current bug
        while  n > student_index and  bug_complexity > students[student_index][0]:
            # Add the current student to the priority queue
            heapq.heappush(available_students, (c[students[student_index][1]-1], students[student_index][1]))
            # Move to the next student
            student_index += 1

        # If the current student is not able to fix the current bug, exit
        if  student_index >= n:
            print("NO")
            return

        # Get the student with the most passes from the priority queue
        _, student_id = heapq.heappop(available_students)

        # Add the current student to the output
        output[bug_id - 1] = student_id

        # Increment the total passes
        total_passes = total_passes + c[student_id - 1]

        # Increment the number of days
        days = days + 1

        # Remove the current student from the list of students
        students.pop(student_index)

    # If the total passes exceed the maximum number of passes, exit
    if not total_passes > s:
        print("YES")
        print(*output)
    else:
        print("NO")

if  __name__ == "__main__":
    main()
