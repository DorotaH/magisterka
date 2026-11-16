def first_repeated_word(str1):
    temp = set()
    for word in str1.split():
        if word not in temp:
            temp.add(word)
        else:
            return word
    return "None"
