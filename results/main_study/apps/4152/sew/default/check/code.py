from  collections import  defaultdict
maxn = 2_000_000_000

mk, bs = [], 1

while  maxn >= bs:
    mk.append(bs)
    bs = bs * 2

n, ls = int(input()), [int(i) for i in input().split()]

dic = defaultdict(int)
for  i in  ls:
    dic[i] += 1

cnt = 0
for  i in  ls:
    dic[i] -= 1
    flag = False
    for  j in  mk:
        if dic[j - i] > 0:
            flag = True
            break

    if  not  flag:
        cnt += 1
    dic[i] += 1

print(cnt)