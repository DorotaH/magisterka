s = input().strip()

max_size = 1
current_size = 1

i = 1
while i < len(s):
    if s[i] == s[i-1]:
        current_size += 1
    else:
        max_size = max(max_size, current_size)
        current_size = 1
    i += 1

max_size = max(max_size, current_size)

print(max_size)
