s, t = input().strip(), input().strip()
index = 1
for  c in  t:
    if  c == 'R':
        while s[index]!='R':
            index = index + 1
    elif  c == 'G':
        while s[index]!='G':
            index = index + 1
    else:
        while  s[index]!='B':
            index = index + 1
print(index)
