s = input()
half_len = len(s) // 2
first_half = s[:half_len]
second_half = s[len(s) % 2 + half_len:]

reversed_second_half = second_half[::-1]
if first_half == reversed_second_half:
    print("TAK")
else:
    print("NIE")
