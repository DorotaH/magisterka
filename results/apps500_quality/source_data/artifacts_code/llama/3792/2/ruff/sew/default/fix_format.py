def solve():
    n, k = map(int, input().split())
    s, t = input(), input()

    c = 0
    same = diff = 0

    for i in range(n):
        if t[i] == s[i]:
            c += 1
            same += 1
        elif s[i] == "a" and t[i] == "b":
            c += 1 + same
        elif s[i] == "b" and t[i] == "a":
            c = c + min(same + 1, k)
            diff = 1

    print(c)


solve()
