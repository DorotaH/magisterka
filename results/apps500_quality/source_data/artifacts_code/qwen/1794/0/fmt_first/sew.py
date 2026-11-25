from sys import stdin, stdout

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

# Initialize the array to store the minimum number of tickets needed
rho = [0] * (n - 1)

# Iterate over each station to calculate the minimum number of tickets needed
for i in range(n - 1):
    rho[i] = a[i] - i - 1

# Calculate the sum of all values rho[i, j] for 1 <= i < j <= n
result = sum(rho[i] * (n - i - 1) for  i in  range(n - 1))

# Print the result
stdout.write(str(result) + "\n")