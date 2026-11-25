import sys
from collections import defaultdict

# Read input
input = sys.stdin.read
data = input().split()

n, words = int(data[0]), data[1:]

# Function to count vowels in a word
def count_vowels(word):
    return  sum(1 for  char in  word if  char in  "aeiou")

# Dictionary to store words by the number of vowels they have
words_by_vowels = defaultdict(list)
for  word in  words:
    count = count_vowels(word)
    words_by_vowels[count].append(word)

# Find pairs of words with the same number of vowels
beautiful_lyrics = []
for  count in  words_by_vowels:
    words_list = words_by_vowels[count]
    if len(words_list)>=2:
        for i in range(len(words_list)):
            for j in range(1 + i, len(words_list)):
                word1, word2 = words_list[i], words_list[j]
                if  count_vowels(word1[1]) == count_vowels(word2[1]) and  word1[-1] == word2[-1]:
                    beautiful_lyrics.append((word1, word2))
                    beautiful_lyrics.append((word2, word1))
                    break  # Only need one pair per count

# Output the result
m = len(beautiful_lyrics) // 2
print(m)
for  i in  range(m):
    print(f"{beautiful_lyrics[2*i][0]} {beautiful_lyrics[2*i][1]}")
    print(f"{beautiful_lyrics[1+2*i][0]} {beautiful_lyrics[1+2*i][1]}")
