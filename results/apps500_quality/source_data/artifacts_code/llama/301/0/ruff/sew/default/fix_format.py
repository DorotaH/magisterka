def find_array():
    u, v = map(int, input().split())
    if u == v == 0:
        print(0)
        return

    ans, i = [], 1
    while u != 0:
        if u & 1:
            if v >= i:
                ans.append(i)
                v -= i
            else:
                print(-1)
                return
        u = u >> 1
        i = i << 1

    print(len(ans))
    print(*ans)


find_array()
