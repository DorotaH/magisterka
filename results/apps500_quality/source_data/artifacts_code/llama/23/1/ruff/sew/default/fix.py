import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
digits = [int(d) for d in str(a)]
digits.sort(reverse=True)

for i in range(len(digits)):
    if  a > b:
        if digits[i]>b-((a % 10) * (len(digits) - i - 1)):
            digits[i], digits[-1] = digits[-1], digits[i]
            break

print(''.join(map(str, digits)))