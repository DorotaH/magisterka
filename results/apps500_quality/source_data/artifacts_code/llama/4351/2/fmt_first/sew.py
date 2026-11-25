n = int(input())
str_n = str(n)
if not str_n == str_n[::-1]:
    print("No")
else:
    print("Yes")