n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))
c = list(map(int, input().split()))

error_diff = set(a) - set(c)
error_diff1, error_diff2 = set(a) - set(b), set(b) - set(c)

if  len(error_diff) == 2:
    print(error_diff.pop(), end=" ")
    print(error_diff.pop())
elif  len(error_diff1) == 1 and len(error_diff2) == 1:
    print(error_diff1.pop(), end=" ")
    print(error_diff2.pop())
else:
    print("No solution")