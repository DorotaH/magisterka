import  math

A, B = map(int, input().split())
min_val = min(A, B)

factorials = [math.factorial(i) for i in range(min_val + 1)]

gcd = factorials[-1]
for i in range(min_val, A):
    gcd=math.gcd(gcd, factorials[i])

for i in range(min_val, B):
    gcd=math.gcd(gcd, factorials[i])

print(gcd)