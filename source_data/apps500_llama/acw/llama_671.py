s = input()
shift = 1 if s == "R" else -1
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
input_string = input()
result = "".join(
	keyboard[(shift + keyboard.index(char)) % 32] for char in input_string
)
print(result)
