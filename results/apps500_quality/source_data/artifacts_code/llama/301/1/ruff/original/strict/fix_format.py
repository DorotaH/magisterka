def solve():
    u, v = map(int, input().split())
    if u == 0:
        if v == 0:
            print(0)
        else:
            print(-1)
        return
    ans = []
    cur = 0
    while v > 0:
        if u >= v and (u == v or v % 2 == 0):
            ans.append(v)
            cur += v
            v = 0
        else:
            v -= 1
            ans.append(1)
            cur += 1
        u -= 1
    if cur != v:
        print(-1)
        return
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    solve()
