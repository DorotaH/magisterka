import sys

# Read input from standard input
direction = sys.stdin.readline().strip()
message = sys.stdin.readline().strip()

# Define the keyboard layout
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

# Create a dictionary to map each character to its index in the keyboard layout
keyboard_index = {char: i for i, char in enumerate(keyboard)}


# Function to shift the message left
def shift_left(message):
    shifted_message = []
    for char in message:
        index = keyboard_index[char]
        if index == 0:
            shifted_message.append(keyboard[-1])
        else:
            shifted_message.append(keyboard[index - 1])
    return "".join(shifted_message)


# Function to shift the message right
def shift_right(message):
    shifted_message = []
    for char in message:
        index = keyboard_index[char]
        if index == len(keyboard) - 1:
            shifted_message.append(keyboard[0])
        else:
            shifted_message.append(keyboard[index + 1])
    return "".join(shifted_message)


# Determine the original message based on the direction of the shift
if direction == "L":
    original_message = shift_left(message)
else:
    original_message = shift_right(message)

# Print the original message
print(original_message)
