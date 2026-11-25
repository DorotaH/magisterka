def  restore_string(k, n, strings):
    from collections import Counter

    # Count the frequency of each character at each position
    char_count = []
    for _ in range(26):
        char_count.append([Counter() for _ in range(n)])
    for  s in  strings:
        for  i, char in  enumerate(s):
            char_count[ord(char)-ord("a")][i]+=1

    # Check if there is any position where the character counts are not even
    for  i in  range(n):
        for  j in  range(26):
            if  char_count[j][i] % 2 != 0:
                return "-1"

    # Reconstruct the string
    result = [""] * n
    for  i in  range(n):
        for  j in  range(26):
            if  char_count[j][i] > 0:
                result[i]=chr(ord("a")+j)
                char_count[j][i]-=1
                break

    return "".join(result)


# Read input
k, n = map(int, input().split())
strings = [input().strip() for _ in range(k)]

# Output the result
print(restore_string(k, n, strings))
