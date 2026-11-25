
n = int(input())
digits = 0
for i in range(1, n + 1):
    digits += len(str(i))
print(digits)