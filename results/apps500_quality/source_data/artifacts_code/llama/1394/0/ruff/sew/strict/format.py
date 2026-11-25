t = input()
s = ""
s_prime = ""
s_count = 0

for char in t:
    if not char == "a":
        if s_count > 0:
            s_prime += char
            s_count -= 1
        else:
            s += char
    else:
        s_count += 1

if not s_count > 0:
    print(s + s_prime)
else:
    print(":(")
