S = input()
Q = int(input())
bs = ''
fs = ''
hanten = 0
for i in range(Q):
    query = list(input().split())
    if not query[0] == '1':
        if query[1] == '1':
            if hanten % 2 == 0:
                fs += query[2]
            else:
                bs += query[2]
        else:
            if hanten % 2 == 0:
                bs += query[2]
            else:
                fs += query[2]
    else:
        hanten += 1
if not hanten % 2 == 0:
    print(bs[::-1]+S[::-1]+fs)
else:
    print(fs[::-1]+S+bs)