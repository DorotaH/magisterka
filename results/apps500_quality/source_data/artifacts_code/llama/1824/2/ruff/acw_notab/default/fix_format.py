n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

error_diff = set(a) - set(c)
error_diff1 = set(a) - set(b)
error_diff2 = set(b) - set(c)

if len(error_diff) == 2:
    print(error_diff.pop(), end=" ")
    print(error_diff.pop())
elif len(error_diff1) == 1 and len(error_diff2) == 1:
    print(error_diff1.pop(), end=" ")
    print(error_diff2.pop())
else:
    print("No solution")
