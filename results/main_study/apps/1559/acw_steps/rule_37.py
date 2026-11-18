l = int(input())
a = input()
la = len(a)
if la % l != 0:
    per = 1+la//l
    ans = '1'+(l-1)*'0'
    ans *= per
    print(ans)
else:
    ans = a[:l]
    per = la//l
    if per*ans > a:print(per*ans)
    else:
        temp = str(1+int(ans))
        if len(temp) == l:print(per*temp)
        else:
            temp = '1'+(l-1)*'0'
            temp *= (per+1)
            print(temp)
