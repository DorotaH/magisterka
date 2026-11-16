def word_len(s):
    s = s.split(" ")
    for word in s:
        return len(word) % 2 == 0
