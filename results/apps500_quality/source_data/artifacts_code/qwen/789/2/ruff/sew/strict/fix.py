n = int(input())
index = 0
count = 0

while count < n:
    num=int("".join(sorted(str(i))))
    if  str(num).count('4') == str(num).count('7'):
        count = count + 1
        if n == count:
            index = i
            break
    i += 1

print(index)
