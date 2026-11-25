def  find_string(t):
    n=len(t)
    for k in range(1, 1 + n):
        if n % k == 0:
            s=t[:k]*(n//k)
            if  all(t[i] == s[i] for  i in  range(n)):
                return  s

T = int(input())
results = []
for _ in range(0, T):
    t = input()
    results.append(find_string(t))

for result in results:
    print(result)