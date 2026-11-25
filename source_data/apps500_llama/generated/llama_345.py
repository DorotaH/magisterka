import math
import sys

n, k = map(int, input().split())

max_winners = math.floor(n / 2)
diplomas = 0
certificates = 0

for diplomas in range(max_winners + 1):
    if diplomas > 0:
        certificates = diplomas * k
    else:
        certificates = 0

    if diplomas + certificates <= n:
        break

winner_count = diplomas + certificates
no_winner_count = n - winner_count
print(diplomas, certificates, no_winner_count)
