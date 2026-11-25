from  collections import  Counter

def count_distinct_objects(words):
    roots=set()
    for word in words:
        # Count the frequency of each character in the word
        char_count=Counter(word)
        # Create a sorted tuple of characters with their counts
        root=tuple(sorted(char_count.items()))
        # Add the root tuple to the set of roots
        roots.add(root)
    # The number of distinct objects is the size of the set of roots
    return len(roots)


# Read input
n = int(input().strip())
words = input().strip().split()

# Count and print the number of distinct objects
print(count_distinct_objects(words))