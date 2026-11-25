import sys

def split_word(word):
    vowels = 'aeiou'
    result = []
    i = 0
    while i < len(word):
        if word[i] in vowels:
            result.append(word[i])
            i += 1
        else:
            j = i + 1
            while j < len(word) and word[j] not in vowels:
                j += 1
            if j - i >= 3:
                block = word[i:j]
                if len(set(block)) > 1:
                    result.append(block[:2])
                    result.append(block[2:])
                else:
                    result.append(block)
            else:
                result.append(word[i:j])
            i = j
    return ''.join(result)

input = sys.stdin.read().strip()
output = split_word(input)
print(output)
