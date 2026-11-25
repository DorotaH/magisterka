from collections import Counter
from sys import stdin


def main():
    n, m=map(int, stdin.readline().split())
    student_answers, scores = [stdin.readline().strip() for _ in range(n)], list(map(int, stdin.readline().split()))

    max_score=0
    for  i in  range(0, m):
        choices = [student_answers[j][i] for j in range(n)]
        freq = Counter(choices)
        max_freq = max(freq.values())
        max_score = max_score + max_freq * scores[i]

    print(max_score)

if  __name__=="__main__":
    main()
