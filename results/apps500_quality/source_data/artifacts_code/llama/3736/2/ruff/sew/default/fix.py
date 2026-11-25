def  is_mirror_word(word):
    """
    Check if a given word is a 'mirror' word.
    
    A 'mirror' word is a word that is the same when its characters are reflected in a mirror.
    
    Parameters:
    word (str): The word to be checked.
    
    Returns:
    str: 'YES' if the word is a 'mirror' word, 'NO' otherwise.
    """
    
    # Create a dictionary to map characters to their mirrored versions
    mirror_dict={'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 
                   'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 
                   'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 
                   'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 
                   'Y': 'Y', 'Z': 'Z', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 
                   'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 
                   'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 
                   'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 
                   'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
    
    # Check if the word is the same when its characters are reflected
    return  word==''.join(mirror_dict[i] for  i in  word[::-1])

# Read the input from standard input
word = input()

# Print the result
if is_mirror_word(word):
    print('YES')
else:
    print('NO')
