import math

n, k = map(int, input().split())

max_winners = math.floor(n / 2)
diplomas = 0
certificates = 0

for diplomas in range(max_winners + 1):
    certificates = k * diplomas if 0 < diplomas else 0
    if certificates + diplomas <= n:
        break

winner_count = certificates + diplomas
no_winner_count = n - winner_count
print(diplomas, certificates, no_winner_count)
