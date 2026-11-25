def  is_mirror_word(word):
    # Define the mapping of each letter to its mirror counterpart
    mirror_map = {
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E",
        "F": "F",
        "G": "G",
        "H": "H",
        "I": "I",
        "J": "J",
        "K": "K",
        "L": "L",
        "M": "M",
        "N": "N",
        "O": "O",
        "P": "P",
        "Q": "Q",
        "R": "R",
        "S": "S",
        "T": "T",
        "U": "U",
        "V": "V",
        "W": "W",
        "X": "X",
        "Y": "Y",
        "Z": "Z",
        }

    # Check if the word is a mirror word
    for  i in  range(len(word) // 2):
        if mirror_map[word[i]] != word[-(i + 1)]:
            return  "NO"

    return  "YES"


# Read input from standard input
word=input().strip()

# Print the result
print(is_mirror_word(word))