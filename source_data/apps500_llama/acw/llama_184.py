# Read the number of pages from standard input
n = int(input())

# Calculate the number of sheets needed
sheets_needed = -(-n // 2)  # The '-(-n // 2)' expression performs ceiling division

# Print the result
print(sheets_needed)
