def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = "".join(word[:-1] + word[-1].upper() + " " for word in str1.split())
    return result[:-1]
