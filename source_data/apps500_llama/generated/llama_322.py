n = int(input())
rounded_n = n + (10 - n % 10) if n % 10 > 5 else n
print(rounded_n)
