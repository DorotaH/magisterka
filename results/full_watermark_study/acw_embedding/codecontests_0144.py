for _ in range(int(input())):
    s = input()

    if len(s)==1:
        print(s)
        continue

    if s[0]==s[len(s)-1]:
        print(s)
    else:
        ns = ""
        ns = 'b' if s[0]=='a' else 'a'
        print(ns+s[1:])