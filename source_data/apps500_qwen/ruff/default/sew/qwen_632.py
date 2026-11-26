n = int(input())
if n < 10:
    digits = n
elif n < 100:
    digits = 9 + (n - 9) * 2
elif n < 1000:
    digits = 9 + 90 * 2 + (n - 99) * 3
else:
    digits = 9 + 90 * 2 + 900 * 3 + (n - 999) * 4
print(digits)
