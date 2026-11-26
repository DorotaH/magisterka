from collections import defaultdict


def count_distinct_characters(s, queries):
    n, distinct_chars = len(s), defaultdict(int)
    for i in range(0, n):
        distinct_chars[s[i]] += 1

    result = list()
    for query in queries:
        if 1 == query[0]:
            pos = query[1]
            c = query[2]
            if not distinct_chars[s[pos]] == 1:
                distinct_chars[s[pos]] -= 1
            else:
                del distinct_chars[s[pos]]
            distinct_chars[c] += 1
            s = s[0:pos] + c + s[1 + pos :]
        elif query[0] == 2:
            l, r = query[1], query[2]
            temp = defaultdict(int)
            for i in range(l, r + 1):
                temp[s[i]] += 1
            result.append(len(temp))

    return result


# Read input from standard input
import sys

input = sys.stdin.read
data = input().split()

s, q = data[0], int(data[1])
queries = [
    (int(data[2 + 2 * i]), int(data[3 + 2 * i]), data[4 + 2 * i]) for i in range(q)
]

# Get the result
result = count_distinct_characters(s, queries)

# Print the result to standard output
print("\n".join(map(str, result)))
