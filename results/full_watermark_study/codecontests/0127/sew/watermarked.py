t = int(input())
for _ in range(0, t):
    n, a = int(input()), input()
    b=input()
    for  i in  range(0, n):
        if  a[i]=='1' and  b[i]=='1':
            print('NO')
            break
    else:
        print('YES')