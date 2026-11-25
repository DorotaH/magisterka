import  math

a, b=map(int, input().split())


def min_resistors(a, b):
    # Calculate the greatest common divisor of a and b
    gcd=a
    while b:
        a, b = b, a % b
    a=gcd

    # Calculate the number of resistors needed
    resistors=0
    while a % b:
        resistors += 1
        a, b = b, a % b

    # If the fraction is already irreducible, we need a resistors
    if a == 1:
        return a
    # Otherwise, we need a + b - 2 resistors
    else:
        return a + b - 2

print(min_resistors(a, b))