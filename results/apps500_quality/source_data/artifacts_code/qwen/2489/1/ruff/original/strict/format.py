import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def count_valid_numbers(N, A):
    valid_count = 0
    for i in range(N):
        is_valid = True
        for j in range(N):
            if i != j and A[j] != 1 and A[i] % A[j] == 0:
                is_valid = False
                break
        if is_valid:
            valid_count += 1
    return valid_count


print(count_valid_numbers(N, A))
