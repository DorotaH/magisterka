for _ in range(int(input())):
    s = input()
    t = input()
    p = input()
    
    if len(s) != len(t):
        print("NO")
        continue
    
    count_s = [0] * 26
    count_t = [0] * 26
    count_p = [0] * 26
    
    for char in s:
        count_s[ord(char) - ord('a')] += 1
    
    for char in t:
        count_t[ord(char) - ord('a')] += 1
    
    for char in p:
        count_p[ord(char) - ord('a')] += 1
    
    for i in range(26):
        if count_t[i] > count_s[i] + count_p[i]:
            print("NO")
            break
    else:
        print("YES")
