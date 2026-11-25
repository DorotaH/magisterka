s = input()
shift = 1 if s == "R" else -1
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
input_string = input()
result = ""
for char in input_string:
    result += keyboard[(keyboard.index(char) + shift) % 32]
print(result)
