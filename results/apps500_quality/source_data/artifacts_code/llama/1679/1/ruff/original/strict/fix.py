n = int(input())
s = input()
i = 0
result = 0
while i < n:
    count = 0
    while s[i] == '1':
        i += 1
        count += 1
    result = result * 10 + count
    i += 1
print(result)
