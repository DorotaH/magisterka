import sys

# Read input from standard input
direction = sys.stdin.readline().strip()
message = sys.stdin.readline().strip()

# Define the keyboard layout
keyboard = "qwertyuiopasdfghjkl; zxcvbnm,./"

# Create a dictionary to map each character to its position
key_positions = {char: idx for idx, char in enumerate(keyboard)}

# Initialize the original message
original_message = ""

# Process each character in the typed message
for char in message:
    # Find the current position of the character
    current_pos = key_positions[char]

    # Calculate the new position based on the direction of shifting
    if direction == 'L':
        new_pos = (current_pos - 1) % len(keyboard)
    elif direction == 'R':
        new_pos = (current_pos + 1) % len(keyboard)

    # Append the character at the new position to the original message
    original_message += keyboard[new_pos]

# Print the original message
print(original_message)
