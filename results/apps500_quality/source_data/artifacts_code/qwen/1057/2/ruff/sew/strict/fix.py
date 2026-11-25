MOD = 998244353

def count_ways(s):
    n = len(s)
    last = {}
    count=0
    for i in range(n):
        if s[i] in last:
            count = (count + i - last[s[i]]) % MOD
        last[s[i]]=i
    return count

n = int(input())
s = input().strip()
print(count_ways(s))
