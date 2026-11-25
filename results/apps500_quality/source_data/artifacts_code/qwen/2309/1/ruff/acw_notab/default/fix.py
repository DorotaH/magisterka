from collections import defaultdict


def count_vowels(word):
    return sum(bool(char in 'aeiou')
           for char in word)


def find_beautiful_lyrics(words):
    word_count = defaultdict(int)
    vowel_count_map = defaultdict(list)

    for word in words:
        word_count[word] += 1
        for i in range(len(word)):
            if word[i] in 'aeiou':
                vowel_count_map[(count_vowels(word[:i + 1]), word[i])].append(word)

    beautiful_lyrics = []
    for (v1, v2), words_list in vowel_count_map.items():
        if 2 <= len(words_list):
            for word1 in words_list:
                for word2 in words_list:
                    if word1 != word2 and word_count[word1] > 0 and 0 < word_count[word2]:
                        beautiful_lyrics.append((word1, word2))
                        word_count[word1] -= 1
                        word_count[word2] -= 1
                        break
                if len(beautiful_lyrics) == len(vowel_count_map) // 2:
                    break
            if len(beautiful_lyrics) == len(vowel_count_map) // 2:
                break

    return beautiful_lyrics


def main():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    beautiful_lyrics = find_beautiful_lyrics(words)
    print(len(beautiful_lyrics))
    for lyric in beautiful_lyrics:
        print(f"{lyric[0]} {lyric[1]}")


if __name__ == "__main__":
    main()
