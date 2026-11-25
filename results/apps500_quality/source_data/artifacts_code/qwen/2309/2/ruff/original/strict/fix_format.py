from collections import defaultdict


def count_vowels(word: str) -> int:
    return sum(1 for char in word if char in "aeiou")


def find_beautiful_lyrics(words: list[str]) -> list[str]:
    n = len(words)
    max_vowels = max(count_vowels(word) for word in words)
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    beautiful_lyrics = []
    used = set()
    for i in range(n):
        if words[i] in used:
            continue
        for j in range(i + 1, n):
            if words[j] in used:
                continue
            if count_vowels(words[i]) == count_vowels(words[j]):
                last_vowel_i = next(c for c in reversed(words[i]) if c in "aeiou")
                last_vowel_j = next(c for c in reversed(words[j]) if c in "aeiou")
                if last_vowel_i == last_vowel_j:
                    beautiful_lyrics.extend([words[i], words[j]])
                    used.add(words[i])
                    used.add(words[j])
                    break

    return beautiful_lyrics


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    words = data[1:]

    beautiful_lyrics = find_beautiful_lyrics(words)
    print(len(beautiful_lyrics) // 2)
    for i in range(0, len(beautiful_lyrics), 2):
        print(beautiful_lyrics[i], beautiful_lyrics[i + 1])


if __name__ == "__main__":
    main()
