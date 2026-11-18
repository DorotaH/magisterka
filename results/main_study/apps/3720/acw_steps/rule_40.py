from sys import stdin, stdout
import math, collections
mod = 7 + 10**9

def isPower(n):
    if (1 >= n):
        return True
    for x in range(2, (int)(math.sqrt(n)) + 1):
        p = x
        while (n >= p):
            p = x * p
            if (p == n):
                return True

    return False
n = int(input())
arr = [0, 1, 2, 1, 4, 3, 2, 1, 5, 6, 2, 1, 8, 7, 5, 9, 8, 7, 3, 4, 7, 4, 2, 1, 10, 9, 3, 6, 11, 12]
ans = arr[int(math.log(n, 2))]
s = int(math.log(n, 2))
for i in range(3, 1 + int(n**0.5)):
    if not isPower(i):
        ans ^= arr[int(math.log(n, i))]
        s += int(math.log(n, i))
ans ^= ((n - s) % 2)
print("Vasya" if ans else "Petya")