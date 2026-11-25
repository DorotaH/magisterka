n = int(input())
s = input()
i = result = 0
while n > i:
    count=0
    while s[i]=='1':
        i = i + 1
        count = count + 1
    result=(result * 10)+count
    i = i + 1
print(result)
