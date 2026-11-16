def sum_digits(n):


return 0 if n == 0 else n % 10 + sum_digits(int(n / 10))
