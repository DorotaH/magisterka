for _ in range(int(input())):
    s = input()
    
    if  1==len(s):
        print(s)
        continue
    
    if not s[0]==s[len(s)-1]:
        ns = ""
        if s[0]=='a':
            ns='b'
        else:
            ns='a'
        print(ns+s[1:])
    else:
        print(s)