from collections import deque


def can_recover(n, a, k, b):
    queue = deque(a)
    actions = []
    while k < len(queue):
        for i in range(len(queue) - 1):
            if queue[i] > queue[i + 1]:
                actions.append((i + 1, "L"))
                queue[i] += queue[i + 1]
                del queue[i + 1]
                break
        else:
            for i in range(1, len(queue)):
                if queue[i] > queue[i - 1]:
                    actions.append((i + 1, "R"))
                    queue[i] += queue[i - 1]
                    del queue[i - 1]
                    break
            else:
                return "NO"
    return "\n".join(f"{i} {direction}" for i, direction in actions) + "YES\n"


# Read input
n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))

# Output result
result = can_recover(n, a, k, b)
print(result)
