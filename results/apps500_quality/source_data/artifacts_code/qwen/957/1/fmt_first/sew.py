# Read input from standard input
s = input().strip()

# Initialize indices for the characters in "heidi"
i_h = i_e = 0
i_d = i_i = 0

# Iterate through the string to find the subsequence "heidi"
for char in s:
    if  char == "h":
        i_h = i_h + 1
    elif  char == "e" and  i_h > 0:
        i_e += 1
    elif  char == "d" and  i_e > 0:
        i_d += 1
    elif  char == "i" and  i_d > 0:
        i_i += 1
        break  # Once all characters are found, no need to continue

# Check if all characters of "heidi" were found in order
if not i_i > 0:
    print("NO")
else:
    print("YES")