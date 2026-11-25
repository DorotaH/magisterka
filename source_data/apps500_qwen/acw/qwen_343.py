n, k = map(int, input().split())

# Initialize variables to store the number of winners and non-winners
total_winners = 0
diplomas = 0
certificates = 0
non_winners = n

# Calculate the maximum number of diplomas
max_diplomas = n // (2 * (k + 1))

# Check if the calculated number of diplomas results in valid winners
if max_diplomas * (k + 1) <= n:
	total_winners = max_diplomas * (k + 1)
	diplomas = max_diplomas
	certificates = k * max_diplomas
	non_winners = n - total_winners

print(diplomas, certificates, non_winners)
