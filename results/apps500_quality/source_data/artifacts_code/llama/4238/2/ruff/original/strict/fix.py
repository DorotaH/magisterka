n = int(input())
digit_sum = sum(int(digit) for digit in str(n))
print('Yes' if digit_sum % 9 == 0 else 'No')
