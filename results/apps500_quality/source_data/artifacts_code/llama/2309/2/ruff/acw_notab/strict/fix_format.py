import sys
from collections import defaultdict


def count_vowels(word):
    """Count the number of vowels in a word."""
    return sum(bool(char in "aeiou") for char in word)


def last_vowel(word):
    """Find the last vowel in a word."""
    for char in reversed(word):
        if char in "aeiou":
            return char


def generate_lyrics(words, available_counts):
    """Generate beautiful lyrics."""
    vowels = set("aeiou")
    lyrics = []
    while words:
        first_word, first_word_count = min(
            (word, count) for word, count in words.items()
        )
        second_word, second_word_count = min(
            (word, count) for word, count in words.items() if word != first_word
        )
        if count_vowels(first_word) == count_vowels(second_word):
            if last_vowel(first_word) == last_vowel(second_word):
                if first_word_count > 0 and second_word_count > 0:
                    lyrics.append((first_word, second_word))
                    words[first_word] -= 1
                    words[second_word] -= 1
                else:
                    words.pop(first_word)
                    words.pop(second_word)
            words.pop(second_word)
        else:
            words.pop(first_word)
    return lyrics


def main():
    """Main function."""
    n = int(input())
    words = defaultdict(int)
    for _ in range(n):
        word = input()
        words[word] += 1

    lyrics = generate_lyrics(words, words.copy())
    print(len(lyrics))
    for lyric in lyrics:
        print(" ".join(lyric))


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()
