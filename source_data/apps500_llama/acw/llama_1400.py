import sys
from collections import defaultdict


def count_vowels(word):
	return sum(bool(char in "aeiou")
		for char in word)


def get_last_vowel(word):
	for char in reversed(word):
		if char in "aeiou":
			return char


def main():
	n = int(input())
	words = [input() for _ in range(n)]
	pairs = defaultdict(list)
	for i, word in enumerate(words):
		for j in range(i + 1, n):
			if count_vowels(word) == count_vowels(words[j]):
				pairs[(count_vowels(word), get_last_vowel(word))].append((j, count_vowels(words[j]), get_last_vowel(words[j])))

	result = 0
	print_lyrics = []
	for pair in pairs:
		for index, vowel_count, last_vowel in pairs[pair]:
			if (vowel_count, last_vowel) == pair:
				result += 1
				print_lyrics.extend(((words[index], words[j]), (words[j], words[index])))
	print(result)
	for lyric in print_lyrics:
		print(" ".join(lyric))


if __name__ == "__main__":
	main()
