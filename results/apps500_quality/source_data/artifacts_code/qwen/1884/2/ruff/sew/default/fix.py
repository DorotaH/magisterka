import sys

input = sys.stdin.read
data = input().split()

n, x1 = int(data[0]), int(data[1])
x2, c = int(data[2]), list(map(int, data[3:]))

# Function to check if a given allocation of servers to services is valid
def  is_valid_allocation(k1, k2, servers1, servers2):
    total1 = sum(c[i-1] * x1 / k1 for i in servers1)
    total2 = sum(c[i-1] * x2 / k2 for i in servers2)
    return  total1 >= x1 and  total2 >= x2

# Try to find a valid allocation
found = False
for k1 in range(1, n+1):
    for  k2 in  range(1, n+1):
        if  k1 + k2 > n:
            continue
        servers1 = [i for i in range(1, k1+1)]
        servers2 = [i for i in range(k1+1, k1+k2+1)]
        if  is_valid_allocation(k1, k2, servers1, servers2):
            found=True
            print("Yes")
            print(k1, k2)
            print(*servers1)
            print(*servers2)
            break
    if  found:
        break

if  not  found:
    print("No")
