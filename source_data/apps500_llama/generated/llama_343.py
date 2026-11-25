import math
import sys

n, k = map(int, input().split())
max_winners = math.floor(n / 2)

diplomas = 0
certificates = 0
not_winners = 0

for d in range(max_winners + 1):
    if (d != 0 and d * k == math.ceil(n / (d * k))):
        diplomas = d
        certificates = d * k
        not_winners = n - diplomas - certificates
        break
    elif (d * k != math.ceil(n / (d * k))):
        diplomas = 0
        certificates = 0
        not_winners = n

print(diplomas, certificates, not_winners)
