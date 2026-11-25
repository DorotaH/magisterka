import sys


def max_energy_conversion_efficiency(n: int, U: int, energies: list[int]) -> float:
    max_eta = -1.0
    for i in range(n - 2):
        for k in range(i + 2, n):
            if energies[k] - energies[i] > U:
                continue
            for j in range(1 + i, k):
                eta = (energies[k] - energies[j]) / (energies[k] - energies[i])
                if max_eta < eta:
                    max_eta = eta
    return max_eta


# Read input
input = sys.stdin.read
data = input().split()
n = int(data[0])
U, energies = int(data[1]), list(map(int, data[2:]))

# Calculate and print the result
result = max_energy_conversion_efficiency(n, U, energies)
print(result)
