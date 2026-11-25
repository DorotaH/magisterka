def restore_sequence(b):
    a = []
    current = 0
    for b_i in b:
        if b_i == 1:
            current += 1
        else:
            current = int('1' + '0' * (b_i - 2) + '1')
        a.append(current)
        current += 1
    return a

# Read input
n = int(input())
b = [int(input()) for _ in range(n)]

# Restore the sequence
a = restore_sequence(b)

# Print the result
for num in a:
    print(num)
