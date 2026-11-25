def fix_typos(word):
    vowels = set("aeiou")
    result = ""
    i = 0

    while i < len(word):
        if word[i] in vowels:
            result += word[i]
            i += 1
        else:
            j = i + 1
            while j < len(word) and word[j] != word[i]:
                j += 1
            result += word[i:j] + " "
            i = j

    return result.strip()


word = input().strip()
print(fix_typos(word))
