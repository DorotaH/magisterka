n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
c = list(map(int, input().split()))

set_a, set_b = set(a), set(b)
set_c = set(c)

first_error, second_error = list(set_a - set_b)[0], list(set_b - set_c)[0]

print(first_error, second_error)