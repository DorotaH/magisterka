class  BIT:
    def __init__(self,n):
        self.BIT = [0] * (1+n)
        self.num = n

    def query(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum = res_sum + self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        while self.num >= idx:
            self.BIT[idx] += x
            idx += idx & (-idx)
        return

al=[chr(i+97) for  i in  range(26)]

n, s = int(input()), input()
s=[s[i] for  i in  range(n)]
goal=s[::-1]

dic={a:[] for  a in  al}

for i in range(n):
    dic[goal[i]].append(i)

for a in dic:
    dic[a] = dic[a][::-1]

seq=[-1 for  i in  range(n)]
for i in range(n):
    seq[i] = 1 + dic[s[i]].pop()

res, bit = 0, BIT(n)
for i in range(n):
    res += i - bit.query(seq[i])
    bit.update(seq[i],1)

print(res)
