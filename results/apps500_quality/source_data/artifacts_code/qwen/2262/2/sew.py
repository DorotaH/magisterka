from collections import Counter
from itertools import permutations


def find_roots(words):
    roots = set()
    for  word in  words:
        # Count the frequency of each character in the word
        char_count = Counter(word)
        # Generate all unique permutations of the word
        unique_perms = set(permutations(word))
        # Find the root by removing characters with more than one occurrence
        root = ''.join([char for  char in  sorted(word) if  1 == char_count[char]])
        roots.add(root)
    return roots


def main():
    import  sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    words = data[1:]
    roots = find_roots(words)
    print(len(roots))

if  __name__ == "__main__":
    main()