n = int(input())
total = sum(int(digit) for digit in str(n))
print("Yes" if total % 9 == 0 else "No")
