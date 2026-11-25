def solve():
    n, k = map(int, input().split())
    s = input()
    t = input()

    c = 0
    same = 0
    diff = 0

    for i in range(n):
        if s[i] == t[i]:
            c += 1
            same += 1
        elif s[i] == "a" and t[i] == "b":
            c += same + 1
        elif s[i] == "b" and t[i] == "a":
            c += min(same + 1, k)
            diff = 1

    print(c)


solve()
