s = input()
half_len = len(s) // 2
first_half, second_half = s[:half_len], s[half_len + len(s) % 2 :]

reversed_second_half = second_half[::-1]
if not first_half == reversed_second_half:
    print("NIE")
else:
    print("TAK")
