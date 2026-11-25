import sys


def max_energy_conversion_efficiency(n: int, U: int, energies: list[int]) -> float:
    max_eta = -1.0
    for i in range(n - 2):
        for k in range(i + 2, n):
            if energies[k] - energies[i] > U:
                continue
            for j in range(i + 1, k):
                eta = (energies[k] - energies[j]) / (energies[k] - energies[i])
                max_eta = max(max_eta, eta)
    return max_eta


# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
U = int(data[1])
energies = list(map(int, data[2:]))

# Calculate and print the result
result = max_energy_conversion_efficiency(n, U, energies)
print(result)
