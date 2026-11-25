s = input()

mid = len(s) // 2
if  len(s) % 2 == 0:
    mid = mid - 1

first_half, second_half = s[:mid], s[mid + 1 :]

if not first_half == second_half[::-1]:
    print("NIE")
else:
    print("TAK")