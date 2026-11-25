import sys

input=sys.stdin.read
data=input().split()
N, A = int(data[0]), list(map(int, data[1:]))


def count_valid_indices(N, A):
    count=0
    for i in range(N):
        valid=True
        for j in range(N):
            if j != i and A[j] != 0 and A[i] % A[j] == 0:
                valid = False
                break
        if  valid:
            count = count + 1
    return  count

result=count_valid_indices(N, A)
print(result)
