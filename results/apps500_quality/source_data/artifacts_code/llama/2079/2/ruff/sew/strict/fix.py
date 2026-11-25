import sys

input = sys.stdin.readline


def solve():
    n=int(input())
    w, s = list(map(int, input().split())), input().strip()

    introverts, extroverts = [0] * n, [0] * n
    free_rows, occupied_rows = [[] for _ in range(n)], [[] for _ in range(n)]

    for i in range(n):
        if not s[i] == '0':
            extroverts[i] = i
        else:
            introverts[i] = i

    free_rows, occupied_rows = sorted(range(n), key=lambda x: w[x]), sorted(range(n), key=lambda x: w[x], reverse=True)

    result, introvert_index = [0] * (2*n), 0
    extrovert_index=0

    for i in range(2*n):
        if not s[i] == '0':
            result[i] = occupied_rows[extrovert_index]
            free_rows[occupied_rows[extrovert_index]].append(result[i])
            extrovert_index += 1
            occupied_rows.pop(0)
        else:
            result[i] = free_rows[introvert_index]
            occupied_rows[free_rows[introvert_index]].append(result[i])
            introvert_index += 1
            free_rows.pop(0)

    print(*result)

solve()
