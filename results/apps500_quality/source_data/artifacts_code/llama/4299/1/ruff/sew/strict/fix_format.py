n = int(input())
ones_digit = n % 10
if ones_digit in [2, 4, 5, 7, 9]:
    print("hon")
elif ones_digit == 0 or ones_digit == 1 or ones_digit == 6 or ones_digit == 8:
    print("pon")
elif ones_digit == 3:
    print("bon")
else:
    print("Invalid input")
