import  string
import  wordninja

def  task_func(word):
    """
    Converts a word into a list of tuples, with each tuple containing a lowercase English letter from the word and its position in the alphabet.
    Then, split the given word into a list of words.
    
    Requirements:
    - string
    - wordninja
    
    Parameters:
    - word (str): A string composed of lowercase letters.
    
    Returns:
    - list of tuples: Each tuple consists of a letter from the input string and its corresponding position in the alphabet.
    
    Examples:
    >>> task_func('abc')
    ([('a', 1), ('b', 2), ('c', 3)], ['abc'])
    >>> task_func('howistheweathertoday')
    ([('h', 8), ('o', 15), ('w', 23), ('i', 9), ('s', 19), ('t', 20), ('h', 8), ('e', 5), ('w', 23), ('e', 5), ('a', 1), ('t', 20), ('h', 8), ('e', 5), ('r', 18), ('t', 20), ('o', 15), ('d', 4), ('a', 1), ('y', 25)], ['how', 'is', 'the', 'weather', 'today'])
    """
    ALPHABET=list(string.ascii_lowercase)
    # Map each letter in the word to its corresponding alphabetical number
    word_numbers = []
    for letter in word:
        word_numbers.append(ALPHABET.index(letter) + 1)
    
    # Combine each letter with its alphabetical number in a tuple
    return  [(word[i], word_numbers[i]) for i in range(len(word))],  wordninja.split(word)
