n, k = map(int, input().split())

# Initialize variables to store the number of winners and non-winners
total_winners = diplomas = 0
certificates, non_winners = 0, n

# Calculate the maximum number of diplomas
max_diplomas = n // (2 * (k + 1))

# Check if the calculated number of diplomas results in valid winners
if max_diplomas * (k + 1) <= n:
    total_winners, diplomas = max_diplomas * (k + 1), max_diplomas
    certificates, non_winners = max_diplomas * k, n - total_winners

print(diplomas, certificates, non_winners)
