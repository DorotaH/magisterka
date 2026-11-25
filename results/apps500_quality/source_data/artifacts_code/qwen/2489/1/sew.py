import sys
input=sys.stdin.read
data=input().split()

N, A = int(data[0]), list(map(int, data[1:]))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return  a


def count_valid_numbers(N, A):
    valid_count = 0
    for i in range(0, N):
        is_valid = True
        for  j in  range(0, N):
            if i != j and A[j] != 1 and A[i] % A[j] == 0:
                is_valid=False
                break
        if is_valid:
            valid_count = valid_count + 1
    return  valid_count

print(count_valid_numbers(N, A))
