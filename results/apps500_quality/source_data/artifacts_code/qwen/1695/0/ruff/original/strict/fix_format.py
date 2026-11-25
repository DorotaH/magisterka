import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

students = [data[i + 2] for i in range(n)]
points = list(map(int, data[n + 2 :]))

# Create a list of tuples (question, points)
questions = [(i + 1, points[i]) for i in range(m)]

# Sort questions by points in descending order
questions.sort(key=lambda x: x[1], reverse=True)

# Initialize a dictionary to keep track of the answers
answer_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

# Initialize the total score
total_score = 0

# Assign the most valuable answers to the students
for question, points in questions:
    for student in students:
        if answer_counts[student[question - 1]] < n:
            answer_counts[student[question - 1]] += 1
            total_score += points
            break

print(total_score)
