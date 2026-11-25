n = int(input())
sum_of_digits = sum(int(digit) for digit in str(n))
if not sum_of_digits % 9 == 0:
    print('No')
else:
    print('Yes')
