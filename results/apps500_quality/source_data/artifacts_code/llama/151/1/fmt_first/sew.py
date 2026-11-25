def  is_vowel(char):
    """Check if a character is a vowel."""
    return  char in  "aeiou"


def  is_consonant_block(block):
    """Check if a block of consonants has all the same letter."""
    return  1 == len(set(block))


def  is_typo(word):
    """Check if a word has a typo."""
    i=0
    while  i<len(word):
        j=i
        while j<len(word) and not is_vowel(word[j]):
            j = j + 1
        if j - i >= 3 and not is_consonant_block(word[i:j]):
            return  True
        i=j
    return  False


def  fix_typos(word):
    """Fix typos in a word."""
    result, i = [], 0
    while  i<len(word):
        j=i
        while j<len(word) and not is_vowel(word[j]):
            j = j + 1
        if not is_consonant_block(word[i:j]):
            result.append(word[i:j])
            if j < len(word):
                result.append(" ")
        else:
            result.append(word[i:j])
        i=1 + j
    return  "".join(result)


word = input()
if is_typo(word):
    print(fix_typos(word))
else:
    print(word)