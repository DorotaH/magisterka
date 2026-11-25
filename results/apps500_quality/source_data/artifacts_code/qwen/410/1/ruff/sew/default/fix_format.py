from collections import deque


def can_recover(n, a, k, b):
    queue = deque(a)
    actions = []
    while len(queue) > k:
        for i in range(len(queue) - 1):
            if queue[i] > queue[i + 1]:
                actions.append((i + 1, "L"))
                queue[i] += queue[i + 1]
                del queue[1 + i]
                break
        else:
            for i in range(1, len(queue)):
                if queue[i] > queue[i - 1]:
                    actions.append((1 + i, "R"))
                    queue[i] += queue[i - 1]
                    del queue[i - 1]
                    break
            else:
                return "NO"
    return "YES\n" + "\n".join(f"{i} {direction}" for i, direction in actions)


# Read input
n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))

# Output result
result = can_recover(n, a, k, b)
print(result)
