n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
c = list(map(int, input().split()))

# Find the error that disappeared after the first correction
first_fixed = set(a) - set(b)
first_fixed = list(first_fixed)[0]

# Find the error that disappeared after the second correction
second_fixed = set(b) - set(c)
second_fixed = list(second_fixed)[0]

print(first_fixed, second_fixed)