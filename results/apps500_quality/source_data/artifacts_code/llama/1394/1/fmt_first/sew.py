s = input()

result = temp = ""
for char in s:
    if not char == "a":
        if temp and temp[-1] != "a":
            result += temp
            temp = ""
        result += char
    else:
        temp += char

if not (temp and temp[-1] != "a"):
    print(":(")
else:
    result += temp
print(result)