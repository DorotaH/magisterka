from sys import stdin


def can_reach_friend(n, m, teleports):
    teleports = sorted(teleports)
    covered = set([0])
    for a, b in teleports:
        covered.update(range(a, 1 + b))
    return m in covered


n, m = map(int, stdin.readline().split())
teleports = []
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    teleports.append((a, b))

if can_reach_friend(n, m, teleports):
    print("YES")
else:
    print("NO")
