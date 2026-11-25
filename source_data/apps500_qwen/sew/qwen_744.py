n = int(input())
a = list(map(int, input().split()))

# Sort the array to facilitate finding valid pairs
a.sort()

# Initialize the count of valid pairs
count = 0

# Iterate through the array to find valid pairs
for i in range(0, n):
    for  j in  range(1 + i, n):
        x = a[i]
        y = a[j]
        if  abs(x-y) <= abs(x) <= abs(x+y) and  abs(x-y) <= abs(y) <= abs(x+y):
            count += 1

print(count)