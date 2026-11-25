n, m = map(int, input().split())
flag = [input() for _ in range(n)]


def check_flag(flag):
    for i in range(n):
        stripe = flag[i]
        if i % 3 == 0:
            if "R" not in stripe or "G" in stripe or "B" in stripe:
                return False
        elif i % 3 == 1:
            if "G" not in stripe or "R" in stripe or "B" in stripe:
                return False
        elif i % 3 == 2:
            if "B" not in stripe or "G" in stripe or "R" in stripe:
                return False
    return True


if check_flag(flag):
    print("YES")
else:
    print("NO")
