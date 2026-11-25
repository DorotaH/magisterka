import math
from collections import deque

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def min_minutes(a1, b1, a2, b2):
    def get_squares(n):
        return n * (n + 1) // 2

    def is_possible(a, b, minutes):
        if (a <= 0 or b <= 0):
            return False

        squares1 = get_squares(a) - get_squares(a // 2)
        squares2 = get_squares(b) - get_squares(b // 3)

        return squares1 == squares2 and minutes == 0

    def dfs(a, b, minutes, queue, target):
        if (is_possible(a, b, minutes)):
            queue.append(((a, b), minutes))

        if (minutes > 0):
            a_half = a
            if a % 2 == 0:
                a_half = a // 2
            queue.append(dfs(a_half, b, minutes - 1, queue, target))
            b_third = b
            if b % 3 == 0:
                b_third = b // 3
            queue.append(dfs(a, b_third, minutes - 1, queue, target))

    queue = deque()
    dfs(a1, b1, 100, queue, (a2, b2))
    queue = sorted(queue, key=lambda x: abs(get_squares(x[0][0]) - get_squares(x[0][0] // 2) - (get_squares(x[1][1]) - get_squares(x[1][1] // 3))))

    if (len(queue) == 0):
        return -1

    return queue[0][1], queue[0][0][0], queue[0][0][1]

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
result, a, b = min_minutes(a1, b1, a2, b2)
print(result)
print(a, b)
