n = int(input())
total = sum(int(digit) for digit in str(n))
print('Yes' if 0 == total % 9 else 'No')