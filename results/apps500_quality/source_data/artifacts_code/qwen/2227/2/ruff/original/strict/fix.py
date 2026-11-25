def count_powerful_substrings(text):
    n = len(text)
    count = 0
    for i in range(n):
        for j in range(i + 5, n + 1):  # At least 5 characters for "heavy"
            substring = text[i:j]
            if substring.startswith("heavy") and substring.endswith("metal"):
                count += 1
    return count

# Read input
text = input().strip()

# Print the result
print(count_powerful_substrings(text))
