def is_berlanese(word):
    vowels = "aeiou"
    n = len(word)

    for i in range(n - 1):
        if word[i] not in "aeiou" and word[i + 1] not in vowels and word[i + 1] != 'n':
            return "NO"

    return "YES"

# Read input
word = input().strip()

# Output the result
print(is_berlanese(word))
