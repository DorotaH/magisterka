s = input()

result = ""
temp = ""
for char in s:
    if char == 'a':
        temp += char
    else:
        if temp and temp[-1] != 'a':
            result += temp
            temp = ""
        result += char

if temp and temp[-1] != 'a':
    result += temp
else:
    print(':(')
print(result)
