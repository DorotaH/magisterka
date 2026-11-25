# Read the number of people
n = int(input())

# Read the coordinates of the people
x = list(map(int, input().split()))

# Calculate the median of the coordinates
median = sorted(x)[n // 2] if n % 2 else (sorted(x)[n // 2 - 1] + sorted(x)[n // 2]) / 2

# Initialize the total stamina
total_stamina = 0

# Calculate the total stamina
for xi in x:
    total_stamina += (xi - median) ** 2

# Print the result
print(int(total_stamina))
