import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

students = []
for i in range(n):
    students.append(data[1 + i])

points = list(map(int, data[n + 1 :]))

# Calculate the frequency of each answer for each question
answer_counts = defaultdict(lambda: [0] * 5)
for student in students:
    for j in range(m):
        if student[j] == "A":
            answer_counts[j][0] += 1
        elif student[j] == "B":
            answer_counts[j][1] += 1
        elif student[j] == "C":
            answer_counts[j][2] += 1
        elif student[j] == "D":
            answer_counts[j][3] += 1
        elif student[j] == "E":
            answer_counts[j][4] += 1

# Calculate the maximum possible total score
max_score = 0
for j in range(m):
    max_correct_students = max(answer_counts[j])
    max_score += max_correct_students * points[j]

print(max_score)
