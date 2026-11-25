def decode_message(direction, typed_message):
    # Define the layout of the keyboard
    keyboard=[
        'qwertyuiop',
        'asdfghjkl;',
        'zxcvbnm,./'
        ]

    # Flatten the keyboard layout into a single string for easier manipulation
    flat_keyboard=''.join(keyboard)

    # Initialize an empty string to store the original message
    original_message=''

    # Iterate over each character in the typed message
    for char in typed_message:
        # Find the index of the current character in the flat keyboard
        index = flat_keyboard.find(char)

        # Determine the new index based on the direction of shifting
        if direction == 'L':
            new_index = index - 1
        else:
            new_index = index + 1

        # Ensure the new index is within the bounds of the flat keyboard
        if 0 <= new_index < len(flat_keyboard):
            # Append the character at the new index to the original message
            original_message += flat_keyboard[new_index]
        else:
            # If the new index is out of bounds, keep the original character
            original_message += char

    # Return the original message
    return original_message

# Read input from standard input
direction = input().strip()
typed_message = input().strip()

# Decode the message and print the result
print(decode_message(direction, typed_message))
