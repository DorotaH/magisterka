s = input()
n = len(s)
if not n % 2 != 0:
    first_half = s[: n // 2]
    second_half = s[n // 2 :]
    second_half = second_half[::-1]
    if first_half == second_half:
        print("TAK")
    else:
        print("NIE")
else:
    print("NIE")
