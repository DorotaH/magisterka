import math
import sys

n, k = map(int, input().split())
max_winners = math.floor(n / 2)

diplomas = 0
certificates = 0
not_winners = 0

for d in range(max_winners + 1):
	if (d != 0 and k * d == math.ceil(n / (k * d))):
		diplomas = d
		certificates = k * d
		not_winners = n - diplomas - certificates
		break
	elif (k * d != math.ceil(n / (k * d))):
		diplomas = 0
		certificates = 0
		not_winners = n

print(diplomas, certificates, not_winners)
