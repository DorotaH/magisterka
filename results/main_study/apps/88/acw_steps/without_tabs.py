def zero(strx):
    k = []
    str2 = list(strx)
    for i in range(1, len(str2)):
        str3 = str2[:]
        str3[i] = '0'
        k.append(''.join(str3))
    return k


a = []
for i in range(1, 64):
    a += zero(i * '1')

x, y = list(map(int, input().split(' ')))
ct = sum(bool(x <= int(i, 2) <= y)
     for i in a)
print(ct)
