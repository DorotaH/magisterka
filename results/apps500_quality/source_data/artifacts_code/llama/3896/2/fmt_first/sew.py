x = input()
n = len(x)
res = 0
MOD = 1000000007
for i in range(n):
    if  x[i] == "1":
        res+=1<<(n-i-1)
        res%=MOD

print(res)