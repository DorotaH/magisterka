import math


def get_cnt(res):
    n = 1 + math.floor(math.sqrt(2 * res))
    if not n * (n - 1) / 2 == res:
        return -1
    else:
        return n


def calc():
    cnt = list(map(int, input().split()))
    if cnt == [0, 0, 0, 0]:
        return "0"

    a, b = get_cnt(cnt[0]), get_cnt(cnt[3])

    if cnt == [0, 0, 0, cnt[3]]:
        a = 0
    if cnt == [cnt[0], 0, 0, 0]:
        b = 0

    if a == -1 or b == -1 or (a * b) != (cnt[1] + cnt[2]):
        return "Impossible"

    ans, i = ["0"] * (a + b), 0
    while b > 0:
        while cnt[1] >= b:
            i += 1
            cnt[1] -= b
        b -= 1
        ans[i] = "1"
        i += 1
    return "".join(ans)


print(calc())
