n, k = map(int, input().split())

remainders = set()

for i in range(1, k + 1):
    remainder = n % i
    if  remainder in  remainders:
        print("No")
        exit()
    remainders.add(remainder)

print("Yes")