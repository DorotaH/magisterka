n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

set_a = set(a)
set_b = set(b)
set_c = set(c)

first_error = list(set_a - set_b)[0]
second_error = list(set_b - set_c)[0]

print(first_error, second_error)
