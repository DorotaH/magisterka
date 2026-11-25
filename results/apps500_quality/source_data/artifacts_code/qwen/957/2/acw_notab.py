def is_fake_news(s):
    i = 0
    for char in s:
        if char == 'h':
            i += 1
            if i in [1, 2, 3]:
                continue
            elif i == 4:
                return "YES"
        elif i > 0:
            i -= 1
    return "NO"


# Read input from standard input
input_string = input().strip()

# Output the result
print(is_fake_news(input_string))
