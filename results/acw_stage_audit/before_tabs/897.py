def is_Word_Present(sentence, word): 
    s = sentence.split(" ")
    return any((i == word) for i in s)
