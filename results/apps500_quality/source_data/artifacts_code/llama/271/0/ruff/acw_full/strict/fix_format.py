n = int(input())
rounded_n = (10 - n % 10) + n if n % 10 > 5 else n
print(rounded_n)
