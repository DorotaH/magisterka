n, k = map(int, input().split())
max_winners = n // 2
diplomas = 0
certificates = 0

if  max_winners>0:
    for d in range(1, 1 + max_winners):
        c = d * k
        if d + c <= max_winners:
            diplomas, certificates = d, c
            break

non_winners = n - (diplomas + certificates)
print(diplomas, certificates, non_winners)