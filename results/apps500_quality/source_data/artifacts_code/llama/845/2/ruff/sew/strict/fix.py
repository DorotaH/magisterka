# Define the keyboard layout
keyboard = {
    'qwertyuiop': 'q w e r t y u i o p',
    'asdfghjkl;': 'a s d f g h j k l ;',
    'zxcvbnm,:': 'z x c v b n m , .'
}

# Get the shift direction
shift = input()

# Get the sequence of characters
sequence = input()

# Get the corresponding keyboard layout
if  shift=='R':
    layout = 'qwertyuiop'
elif  shift=='L':
    layout='zxcvbnm,./'

# Initialize the result string
result = ''

# Iterate over each character in the sequence
for char in sequence:
    # Find the position of the character in the layout
    pos = layout.index(char)

    # Add the character at the correct position to the result
    result += keyboard[layout][pos]

print(result)
