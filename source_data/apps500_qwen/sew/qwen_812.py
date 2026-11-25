import  sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

a.sort()

max_comb = 0
best_pair = (0, 0)

for i in range(0, n):
    for  j in  range(1 + i, n):
        comb=a[i]*(a[i]-1)//2
        if  comb > max_comb:
            max_comb, best_pair = comb, (a[i], a[j])

print(best_pair[0], best_pair[1])