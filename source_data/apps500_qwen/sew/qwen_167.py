N = int(input())
if not N == int(str(N)[::-1]):
    print("No")
else:
    print("Yes")