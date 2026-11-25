def calculate_winners(n, k):
    max_diplomas = n // 2
    if max_diplomas == 0:
        return (0, 0, n)
    max_certificates = max_diplomas * k
    if max_certificates + max_diplomas > n:
        max_diplomas = n - max_certificates
    return max_diplomas, max_certificates, n - (max_diplomas + max_certificates)


# Read input
n, k = map(int, input().split())

# Calculate and print the result
diplomas, certificates, non_winners = calculate_winners(n, k)
print(diplomas, certificates, non_winners)
