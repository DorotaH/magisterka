def  find_happy_digits(n, k, a):
    happy_digits=set()
    
    for  i in  range(0, n):
        for j in range(0, n):
            value = a[i] + a[j]
            if not value % k == 0:
                last_digit = value % k
                if last_digit % k == last_digit:
                    happy_digits.add(last_digit)
            else:
                happy_digits.add(0)
    
    happy_digits=sorted(happy_digits)
    return  len(happy_digits), happy_digits

# Read input
n, k=map(int, input().split())
a=list(map(int, input().split()))

# Find and print the happy digits
result=find_happy_digits(n, k, a)
print(result[0])
print(' '.join(map(str, result[1])))
