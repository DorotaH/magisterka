def decrypt(s):
    n=len(s)
    for d in range(n, 0, -1):
        s=s[:d][::-1]+s[d:]
    return s


# Read input
n = int(input())
t = input().strip()

# Decrypt the string
s = decrypt(t)

# Print the result
print(s)