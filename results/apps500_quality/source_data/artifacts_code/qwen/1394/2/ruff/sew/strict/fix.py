def  find_s(t):
    n = len(t)
    for  i in  range(n // 2 + 1):
        s, s_prime = t[:i], t[i:].replace('a', '')
        if s+s_prime==t:
            return  s
    return  ":("

# Read input from standard input
t=input().strip()

# Find and print the result
result=find_s(t)
print(result)
