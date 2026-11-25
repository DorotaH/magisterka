# Define the keyboard layout
keyboard = {
    "qwertyuiop": "qwertyuiop",
    "asdfghjkl;": "asdfghjkl;",
    "zxcvbnm,./": "zxcvbnm,./",
}

# Define the current keyboard layout based on the given shift
shift = input()
keyboard_layout = keyboard["qwertyuiop"] if shift == "L" else keyboard["zxcvbnm,./"]

# Read the input string
s = input()

# Initialize the result string
result = ""

# Iterate over the characters in the input string
for c in s:
    # Find the position of the character in the keyboard layout
    for i in range(len(keyboard_layout)):
        if c == keyboard_layout[i]:
            # Calculate the new position of the character after shifting
            new_pos = (i - 3 if shift == "L" else i + 3) % len(keyboard_layout)
            # Append the character at the new position to the result
            result += keyboard_layout[new_pos]
            break

# Print the result
print(result)
