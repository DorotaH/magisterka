def is_berlanese(word):
    vowels = "aeiou"
    for i in range(len(word) - 1):
        if word[i] not in vowels and word[i + 1] != "n" and word[i + 1] not in vowels:
            return "NO"
    return "YES"


# Read input
word = input().strip()

# Output the result
print(is_berlanese(word))
