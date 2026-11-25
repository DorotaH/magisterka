n, total_digits = int(input()), 0

if  n<10:
    total_digits=n * 1
elif  n<100:
    total_digits = 9 * 1 + (n - 9) * 2
elif  n<1000:
    total_digits = 9 * 1 + 90 * 2 + (n - 99) * 3
else:
    total_digits = 9 * 1 + 90 * 2 + 900 * 3 + (n - 999) * 4

print(total_digits)