def decode(s):
    num, i = "", 0
    while i < len(s):
        cnt = 0
        while i < len(s) and s[i] == "1":
            cnt += 1
            i += 1
        num += str(cnt)
        i += 1  # add 1 to move to the next digit separator
    return int(num)


n = int(input())
s = input()
print(decode(s))
