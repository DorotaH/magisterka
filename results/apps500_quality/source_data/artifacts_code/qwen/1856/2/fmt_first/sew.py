from  collections import  defaultdict


def min_passwords(n, passwords):
    # Create a dictionary to count the frequency of each character in all passwords
    char_count=defaultdict(int)
    for password in passwords:
        for char in set(password):
            char_count[char]+=1

    # The minimal number of passwords required is the number of distinct characters that appear in at least one password
    return  len([char for  char, count in  char_count.items() if  count>0])


# Read input
n=int(input())
passwords = [input().strip() for _ in range(n)]

# Calculate and print the result
print(min_passwords(n, passwords))