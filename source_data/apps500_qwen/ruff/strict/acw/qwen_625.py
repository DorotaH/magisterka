def is_berlanese(word):
    vowels = set("aeiou")
    n = len(word)
    return next(
        (
            "NO"
            for i in range(n)
            if word[i] not in vowels
            and i + 1 < n
            and (word[i + 1] not in vowels and word[i + 1] != "n")
        ),
        "YES",
    )


# Read input
word = input().strip()

# Output the result
print(is_berlanese(word))
