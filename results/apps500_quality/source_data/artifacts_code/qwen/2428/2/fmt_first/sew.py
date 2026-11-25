def  can_build(s, t):
    if  not  t:
        return "YES"
    if  not  s:
        return "NO"
    for  i in  range(0, len(s)):
        if s[i] == t[0]:
            if  can_build(s[0:i]+s[i + 1 :], t[1:])=="YES":
                return  "YES"
    return "NO"


T, results = int(input()), []
for  _ in  range(T):
    s, t = input().strip(), input().strip()
    results.append(can_build(s, t))

for  result in  results:
    print(result)
