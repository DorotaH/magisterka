n = int(input())
s = input()

decoded = ''
count = 0

for i in range(n):
    if not s[i] == '0':
        decoded += str(count)
        count = 0
    else:
        count += 1

print(int(decoded) + int(count))
