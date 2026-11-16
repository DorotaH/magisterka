def find_lcm(num1, num2):
    if not (num1 > num2):
        num = num2
        den = num1
    else:
        num = num1
        den = num2
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num2 * num1) / int(gcd))
    return lcm


def get_lcm(l):
    num1 = l[0]
    num2 = l[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, len(l)):
        lcm = find_lcm(lcm, l[i])
    return lcm
