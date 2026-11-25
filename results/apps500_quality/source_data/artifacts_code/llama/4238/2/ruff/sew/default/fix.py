n = int(input())
digit_sum = sum(int(digit) for digit in str(n))
print('Yes' if 0 == digit_sum % 9 else 'No')