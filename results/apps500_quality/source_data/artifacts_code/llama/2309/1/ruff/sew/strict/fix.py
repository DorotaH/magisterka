from collections import defaultdict


def  count_vowels(word):
    count = 0
    for  char in  word:
        if char in "aeiou":
            count = count + 1
    return count


def  get_last_vowel(word):
    for  char in  reversed(word):
        if char in "aeiou":
            return  char


def  main():
    n = int(input())
    words = [input() for _ in range(n)]

    pairs = defaultdict(list)
    for  i, word in  enumerate(words, 0):
        for  j in  range(1 + i, n):
            if  count_vowels(word) == count_vowels(words[j]):
                pairs[(count_vowels(word), get_last_vowel(word))].append((j, count_vowels(words[j]), get_last_vowel(words[j])))

    result, print_lyrics = 0, []
    for  pair in  pairs:
        for  index, vowel_count, last_vowel in  pairs[pair]:
            if  (vowel_count, last_vowel) == pair:
                result += 1
                print_lyrics.append((words[index], words[j]))
                print_lyrics.append((words[j], words[index]))

    print(result)
    for  lyric in  print_lyrics:
        print(" ".join(lyric))

if  __name__=="__main__":
    main()
