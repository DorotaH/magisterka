n = int(input())
rounded_n = (10 - n % 10) + n if 5 < n % 10 else n
print(rounded_n)
