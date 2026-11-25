n, k = map(int, input().split())
max_winners = n // 2
diplomas = 0
certificates = 0

if max_winners > 0:
    for d in range(1, max_winners + 1):
        c = k * d
        if c + d <= max_winners:
            diplomas = d
            certificates = c
            break

non_winners = n - (certificates + diplomas)
print(diplomas, certificates, non_winners)
