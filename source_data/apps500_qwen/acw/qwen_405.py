# Read input from standard input
s = input().strip()
t = input().strip()

# Initialize the position of Liss
position = 1

# Process each instruction
for instruction in t:
	if position < len(s) and s[position] == instruction:
		position += 1

# Output the final position of Liss
print(position)
