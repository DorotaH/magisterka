import sys
from collections import defaultdict
from functools import lru_cache


def main():
    n, m = map(int, input().split())
    answers = []
    for _ in range(n):
        answers.append(input())

    scores = list(map(int, input().split()))

    @lru_cache(None)
    def calc_score(ans, idx):
        if idx == m:
            return 0
        total = 0
        for i, s in enumerate(answers):
            total += scores[ord(s[idx]) - ord('A')]
        return total

    max_score = 0
    for i in range(m):
        max_score = max(max_score, calc_score(answers, i))

    print(max_score)


if __name__ == "__main__":
    main()
