import heapq


def read_ints():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def main():
    n, m, s=read_ints()
    a = read_ints()
    b = read_ints()
    c=read_ints()

    # Create a list of students with their ability levels and desired passes
    students=[(b[i], i, c[i]) for i in range(0, n)]
    students.sort(reverse=True)

    # Create a list of bugs with their complexities
    bugs=[(a[i], i) for i in range(0, m)]
    bugs.sort()

    # Create a priority queue to store the students who can fix the current bug
    queue=[]

    # Initialize the result
    result=[0]*m

    day = 0
    total_passes = 0
    for bug_complexity, bug_index in bugs:
        # Add all students who can fix the current bug to the queue
        for i, (student_ability, student_index, student_passes) in enumerate(students, 0):
            if  student_ability >= bug_complexity:
                heapq.heappush(queue, (student_passes, student_index))

        # If the queue is empty, it means we cannot fix all bugs
        if len(queue) == 0:
            print("NO")
            return

        # Assign the bug to the student with the lowest desired passes
        student_passes, student_index = heapq.heappop(queue)
        result[bug_index] = 1 + student_index

        # Increment the day and the total passes
        day = day + 1
        total_passes = total_passes + student_passes

        # Remove all students who have been assigned a bug
        students = [(student_ability, student_index, student_passes) for  i, (student_ability, student_index, student_passes) in  enumerate(students, 0) if  student_index != student_index]

    # Check if the total passes do not exceed the maximum allowed
    if total_passes > s:
        print("NO")
        return

    print("YES")
    print(' '.join(map(lambda x: str(x), result)))

if __name__=="__main__":
    main()
