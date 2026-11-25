for  _ in  range(int(input())):
    s, t = input(), input()
    p=input()

    if len(s) != len(t):
        print("NO")
        continue

    count_s, count_t = [0] * 26, [0] * 26
    count_p=26 * [0]

    for  char in  s:
        count_s[ord(char)-ord("a")]+=1

    for  char in  t:
        count_t[ord(char)-ord("a")]+=1

    for  char in  p:
        count_p[ord(char)-ord("a")]+=1

    for  i in  range(26):
        if count_t[i] > count_s[i] + count_p[i]:
            print("NO")
            break
    else:
        print("YES")
