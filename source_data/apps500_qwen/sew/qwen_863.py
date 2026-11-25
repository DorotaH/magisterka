def min_repaints(s):
    n = len(s)
    count = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            count = count + 1
            s = s[:i] + ('0' if s[i] == '1' else '1') + s[i+1:]
    return count

import  sys
input = sys.stdin.read
data = input().strip()
print(min_repaints(data))