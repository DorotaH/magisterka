from collections import Counter

n, m = map(int, input().split())
answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Count the frequency of each answer for each question
answer_counts = [Counter() for  _ in  range(m)]
for  answer in  answers:
    for j, char in enumerate(answer):
        answer_counts[j][char] += 1

# Calculate the maximum possible score
max_score = 0
for  j in  range(m):
    # The maximum score for question j is the score of the most frequent answer
    max_score+=answer_counts[j].most_common(1)[0][1] * points[j]

print(max_score)
