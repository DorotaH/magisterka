n, a = int(input()), list(map(int, input().split()))

# Sort the sequence in ascending order
a.sort()

# The maximum possible value of B - C is the sum of the largest numbers in the sequence
max_B_minus_C = sum(a, 0)

print(max_B_minus_C)