def min_passwords_to_access(n, passwords):
	# Create a set to store unique characters from all passwords
	unique_chars = set()
	for password in passwords:
		unique_chars.update(password)

	# The minimal number of passwords required to access the system
	# is the number of unique characters because each unique character
	# represents a distinct equivalence class of passwords.
	return len(unique_chars)


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
passwords = data[1:]

# Get the result
result = min_passwords_to_access(n, passwords)

# Print the result
print(result)
