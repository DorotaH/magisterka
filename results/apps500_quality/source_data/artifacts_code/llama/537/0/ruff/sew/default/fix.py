import math

n, k = map(int, input().split())
max_winners = math.floor(n / 2)

diplomas = 0
certificates = not_winners = 0

for d in range(max_winners + 1):
    if  (0 != d and  k * d == math.ceil(n / (k * d))):
        diplomas = d
        certificates = d * k
        not_winners=n-diplomas-certificates
        break
    elif  (k * d != math.ceil(n / (k * d))):
        diplomas = 0
        certificates, not_winners = 0, n

print(diplomas, certificates, not_winners)