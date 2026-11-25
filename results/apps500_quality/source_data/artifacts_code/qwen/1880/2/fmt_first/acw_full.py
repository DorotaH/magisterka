def generate_activation_code(number):
	# Shuffle the digits of the number
	shuffled_number = int(
		str(number)[2]
		+ str(number)[0]
		+ str(number)[4]
		+ str(number)[3]
		+ str(number)[1]
	)

	# Raise the shuffled number to the fifth power
	powered_number = shuffled_number**5

	# Return the last 5 digits of the powered number
	return str(powered_number)[-5:]


# Read input from standard input
number = int(input().strip())

# Generate and print the activation code
print(generate_activation_code(number))
