def restore_sequence(n, b):
    a = []
    for i in range(n):
        if b[i] == 1:
            a.append(1)
        else:
            carry = 0
            num = b[i]
            while num > 0:
                digit = num % 10
                if digit == 0:
                    digit = 9
                    carry += 1
                num -= digit
            a.append(int('1' * (len(str(b[i])) + carry) + '0' * (len(str(b[i])) - carry)))
    return a

# Read input
n = int(input().strip())
b = [int(input().strip()) for _ in range(n)]

# Restore the sequence
a = restore_sequence(n, b)

# Print the result
for num in a:
    print(num)
