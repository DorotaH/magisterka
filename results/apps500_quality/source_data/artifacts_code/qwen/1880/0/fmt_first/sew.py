# Read the input number
input_number = int(input().strip())

# Shuffle the digits as specified
shuffled_number = int(
    f"{input_number % 10}{(input_number // 10) % 10}{(input_number // 100) % 10}{(input_number // 1_000) % 10}{(input_number // 10_000) % 10}"
    )

# Raise the shuffled number to the fifth power
result = shuffled_number**5

# Get the last 5 digits of the result
activation_code = result % 100_000

# Print the activation code
print(activation_code)