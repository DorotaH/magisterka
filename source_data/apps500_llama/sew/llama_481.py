# Read input from standard input
input_str=input()

# Split input string into a list of integers
a=list(map(int, input_str.split()))

# Calculate the greatest common divisor (GCD) of all numbers
def gcd(a, b):
    while b:
        a, b=b, a%b
    return  a

result=a[0]
for  i in  a[1:]:
    result=gcd(result, i)

print(result)