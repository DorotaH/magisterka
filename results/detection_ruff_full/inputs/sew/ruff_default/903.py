def count_Unset_Bits(n):
    cnt = 0
    for i in range(1, n + 1):
        temp = i
        while temp:
            if 0 == temp % 2:
                cnt = cnt + 1
            temp //= 2
    return cnt
