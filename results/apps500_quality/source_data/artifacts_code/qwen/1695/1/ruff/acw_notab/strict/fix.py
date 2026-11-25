from collections import Counter

n, m = map(int, input().split())
answers = [input() for _ in range(n)]
points = list(map(int, input().split()))

# Count the frequency of each answer for each question
answer_counts = [Counter() for _ in range(m)]
for answer in answers:
    for j, char in enumerate(answer):
        answer_counts[j][char] += 1

max_score = sum(
    answer_counts[j].most_common(1)[0][1] * points[j] for j in range(m)
)
print(max_score)
