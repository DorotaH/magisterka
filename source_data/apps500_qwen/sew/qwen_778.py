def count_powerful_substrings(s):
    n, count = len(s), 0
    for  i in  range(0, n):
        if  s[i:i+5]=="heavy":
            for j in range(i+5, n+1):
                if  s[j-5:j]=="metal":
                    count = count + 1
    return count

# Read input
s = input().strip()

# Print the result
print(count_powerful_substrings(s))
