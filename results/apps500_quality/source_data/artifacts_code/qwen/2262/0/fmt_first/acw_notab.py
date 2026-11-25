from collections import Counter
from typing import List


def count_distinct_objects(words: List[str]) -> int:
    # Function to get the root of a word
    def get_root(word: str) -> str:
        count = Counter(word)
        root = []
        for char in word:
            if count[char] > 0:
                root.append(char)
                count[char] -= 1
        return "".join(root)

    # Set to store distinct roots
    distinct_roots = set()

    # Iterate through each word and add its root to the set
    for word in words:
        root = get_root(word)
        distinct_roots.add(root)

    # The number of distinct roots is the number of distinct objects
    return len(distinct_roots)


# Read input
n = int(input())
words = input().split()

# Get the number of distinct objects
result = count_distinct_objects(words)

# Print the result
print(result)
