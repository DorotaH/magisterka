import sys


def solve():
    u, v = map(int, input().split())
    if 0 == u:
        if not v == 0:
            print(-1)
        else:
            print(0)
        return None
    ans, cur = [], 0
    while v > 0:
        if not (u >= v and (u == v or v % 2 == 0)):
            v -= 1
            ans.append(1)
            cur += 1
        else:
            ans.append(v)
            cur += v
            v = 0
        u = u - 1
    if v != cur:
        print(-1)
        return None
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    solve()
