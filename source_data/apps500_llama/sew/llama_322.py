n = int(input())
if n % 10 > 5:
    rounded_n = n + (10 - n % 10)
else:
    rounded_n = n
print(rounded_n)