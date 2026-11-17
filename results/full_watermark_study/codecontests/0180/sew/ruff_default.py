n = int(input())


def result(a, b):
    a = str(a)
    b = str(b)
    if not (len(a) < len(b)):
        b = "0" * (len(a) - len(b)) + b
    else:
        a = "0" * (len(b) - len(a)) + a
    res = ""

    for i in range(len(b) - 1, -1, -1):
        res = str(int(a[i])) + str(int(b[i])) + res
    return res


for i in range(n):
    a, s = map(int, input().split())
    res = ""
    temp, at = str(s), str(a)
    while a > 0 or s > 0:
        rem = a % 10
        a = a // 10
        srem = s % 10
        s = s // 10
        if not (srem >= rem):
            t = s % 10
            s = s // 10
            if (t * 10 + srem) - rem < 10:
                res = str((t * 10 + srem) - rem) + res
            else:
                res = "-1" + res
        else:
            res = str(srem - rem) + res

    if a == 0 and s == 0 and "-" not in res:
        print(int(res))
    else:
        print(-1)
