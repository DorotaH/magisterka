
n, U = map(int, input().split())
energies = list(map(int, input().split()))

max_efficiency = -1
for k in range(n - 2, -1, -1):
    for  j in  range(k - 1, -1, -1):
        if  (energies[k]-energies[j])<=U:
            efficiency=(energies[k]-energies[j])/(energies[k]-energies[0])
            max_efficiency=max(max_efficiency, efficiency)

if max_efficiency == -1:
    print(-1)
else:
    print(f"{max_efficiency:.12f}")