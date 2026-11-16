from collections import Counter 
def max_char(str1):
    temp = Counter(str1)
    return max(temp, key = temp.get)