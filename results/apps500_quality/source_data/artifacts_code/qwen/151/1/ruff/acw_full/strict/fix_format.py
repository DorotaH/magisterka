def insert_spaces(word):
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    i = 0
    while i < len(word):
        if word[i] in vowels:
            result.append(word[i])
            i += 1
        else:
            consonants = []
            while i < len(word) and word[i] not in vowels:
                consonants.append(word[i])
                i += 1
            if len(consonants) >= 3 and len(set(consonants)) >= 2:
                # Find the longest valid block of consonants
                start = 0
                while len(consonants) > start and consonants[start] == consonants[0]:
                    start += 1
                result.extend(
                    ("".join(consonants[:start]), " ".join(consonants[start:]))
                )
            else:
                result.append("".join(consonants))
    return "".join(result)


# Read input from standard input
word = input().strip()

# Print the result
print(insert_spaces(word))
