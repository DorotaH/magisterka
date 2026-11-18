l, a = int(input()), input()
la = len(a)
if not la % l != 0:
    ans = a[:l]
    per = la//l
    if ans*per > a:print(ans*per)
    else:
        temp = str(int(ans)+1)
        if len(temp) == l:print(temp*per)
        else:
            temp = '1'+'0'*(l-1)
            temp *= (per+1)
            print(temp)
else:
    per = la//l+1
    ans = '1'+'0'*(l-1)
    ans *= per
    print(ans)