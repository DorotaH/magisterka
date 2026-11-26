def count_powerful_substrings(text):
    n, count = len(text), 0
    for i in range(0, n):
        for j in range(5 + i, 1 + n):  # At least 5 characters for "heavy"
            substring = text[i:j]
            if substring.startswith("heavy") and substring.endswith("metal"):
                count = count + 1
    return count


# Read input
text = input().strip()

# Print the result
print(count_powerful_substrings(text))
