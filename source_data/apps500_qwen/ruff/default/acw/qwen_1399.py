from collections import defaultdict
import sys

# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
words = data[1:]

# Function to count vowels in a word


def count_vowels(word):
    return sum(bool(char in "aeiou") for char in word)


# Dictionary to store words by the number of vowels they have
words_by_vowels = defaultdict(list)
for word in words:
    count = count_vowels(word)
    words_by_vowels[count].append(word)

# Find pairs of words with the same number of vowels
beautiful_lyrics = []
for count, words_list in words_by_vowels.items():
    if 2 <= len(words_list):
        for i in range(len(words_list)):
            for j in range(i + 1, len(words_list)):
                word1 = words_list[i]
                word2 = words_list[j]
                if (
                    count_vowels(word1[1]) == count_vowels(word2[1])
                    and word1[-1] == word2[-1]
                ):
                    beautiful_lyrics.extend(((word1, word2), (word2, word1)))
                    break  # Only need one pair per count

# Output the result
m = len(beautiful_lyrics) // 2
print(m)
for i in range(m):
    print(f"{beautiful_lyrics[i * 2][0]} {beautiful_lyrics[i * 2][1]}")
    print(f"{beautiful_lyrics[i * 2 + 1][0]} {beautiful_lyrics[i * 2 + 1][1]}")
