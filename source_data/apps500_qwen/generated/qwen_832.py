def find_happy_digits(n, k, a):
    happy_digits = set()
    
    for i in range(n):
        for j in range(n):
            value = a[i] + a[j]
            if value % k == 0:
                happy_digits.add(0)
            else:
                last_digit = value % k
                if last_digit % k == last_digit:
                    happy_digits.add(last_digit)
    
    happy_digits = sorted(happy_digits)
    return len(happy_digits), happy_digits

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Find and print the happy digits
result = find_happy_digits(n, k, a)
print(result[0])
print(' '.join(map(str, result[1])))
