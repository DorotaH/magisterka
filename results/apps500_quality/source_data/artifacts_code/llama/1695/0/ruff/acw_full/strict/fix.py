from sys import stdin

n, m = map(int, stdin.readline().split())
students = [stdin.readline().strip() for _ in range(n)]
answers = list(map(int, stdin.readline().split()))

# Transpose the students answers
students_transposed = list(map(''.join, zip(*students)))

# Find the maximum frequency of each character
max_frequencies = [max(map(lambda x: x.count(c), students_transposed)) for c in 'ABCDE']

# Calculate the maximum possible score for each question
max_scores = [min(a * f, a) for a, f in zip(answers, max_frequencies)]

# Sum the maximum scores to get the total
total_score = sum(max_scores)

print(total_score)
