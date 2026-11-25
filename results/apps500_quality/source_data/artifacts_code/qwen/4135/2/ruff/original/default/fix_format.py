def decrypt_string(t):
    n = len(t)
    s = list(t)
    for d in range(n, 0, -1):
        s[:d] = reversed(s[:d])
    return "".join(s)


# Read input
n = int(input().strip())
t = input().strip()

# Decrypt the string
decrypted_string = decrypt_string(t)

# Print the result
print(decrypted_string)
