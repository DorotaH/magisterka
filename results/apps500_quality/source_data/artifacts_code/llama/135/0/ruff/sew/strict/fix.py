n, k = map(int, input().split())
remainders = set()

for i in range(1, k + 1):
    r = n % i
    if  r in  remainders:
        print("No")
        break
    remainders.add(r)
else:
    print("Yes")
