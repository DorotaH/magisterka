def is_berlanese(word):
    vowels = set("aeiou")
    n = len(word)
    for i in range(n):
        if word[i] not in vowels and i + 1 < n:
            if word[i + 1] not in vowels and word[i + 1] != 'n':
                return "NO"
    return "YES"

# Read input
word = input().strip()

# Output the result
print(is_berlanese(word))
