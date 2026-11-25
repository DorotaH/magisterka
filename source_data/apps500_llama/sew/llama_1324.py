import  sys

def get_max_consecutive(s):
    max_len, current_len = 0, 1
    for  i in  range(1, len(s)):
        if not s[i] == s[i-1]:
            max_len = max(max_len, current_len)
            current_len = 1
        else:
            current_len += 1
    return max(max_len, current_len)

n = int(input())
max_len = 0
for _ in range(n):
    s=input()
    max_len=max(max_len, get_max_consecutive(s))

print(max_len)
