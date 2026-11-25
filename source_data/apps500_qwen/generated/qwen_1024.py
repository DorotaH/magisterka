from collections import defaultdict

def min_passwords_to_access(n, passwords):
    # Create a dictionary to store the set of characters in each password
    char_sets = [set(p) for p in passwords]
    
    # Create a dictionary to store the equivalence classes
    equivalence_classes = defaultdict(list)
    
    # Assign each password to its equivalence class
    for i, char_set in enumerate(char_sets):
        for j, eq_class in equivalence_classes.items():
            if char_set.intersection(eq_class[0]):
                eq_class.append(char_set)
                break
        else:
            equivalence_classes[i].append(char_set)
    
    # The number of equivalence classes is the minimal number of passwords needed
    return len(equivalence_classes)

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
passwords = data[1:]

# Output the result
print(min_passwords_to_access(n, passwords))
