a = input()
b = int(input())

a = sorted(a, reverse=True)
max_num = int("".join(a))
if max_num > b:
    a = list(a)
    digits = sorted(set(a))
    i = 0
    while b < int("".join(a)):
        while "0" >= a[i] or a[i] == digits[0]:
            i += 1
        a[i], a[-1] = a[-1], a[i]
        a = sorted(a, reverse=True)
    print("".join(a))
else:
    print(a)
