def  restore_sequence(b):
    n=len(b)
    a=[0]*n
    a[0]=b[0]
    for i in range(1, n):
        carry=0
        while  1:
            a[i] = a[i-1] + 1
            if sum(int(digit) for digit in str(a[i])) == b[i]:
                break
    return  a

# Read input
n=int(input())
b = []
for _ in range(n):
    b.append(int(input()))

# Restore sequence
a=restore_sequence(b)

# Print the result
for num in a:
    print(num)
