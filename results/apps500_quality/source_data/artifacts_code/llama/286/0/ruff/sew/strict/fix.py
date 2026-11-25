import math

n = int(input())
ans = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if  n % i == 0:
        ans = ans + 2
        if i!=n//i:
            ans = ans + 1
print(ans)
