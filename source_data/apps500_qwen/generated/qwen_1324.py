def max_beauty(n, strings):
    result = ""
    for s in strings:
        result = result + s + s[-1]
    max_len = 0
    current_len = 1
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    max_len = max(max_len, current_len)
    return max_len

# Read input
n = int(input().strip())
strings = [input().strip() for _ in range(n)]

# Calculate and print the result
print(max_beauty(n, strings))
