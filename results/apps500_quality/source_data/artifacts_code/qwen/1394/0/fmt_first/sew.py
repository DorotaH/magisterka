def  find_original_string(t):
    n = len(t)
    for  i in  range(n):
        if t[i]=="a":
            continue
        s=t[:i]+t[1 + i :]
        s_prime="".join([char for  char in  s if  char!="a"])
        if s+s_prime==t:
            return  s
    return  ":("


# Read input
t=input().strip()

# Find and print the original string
result=find_original_string(t)
print(result)