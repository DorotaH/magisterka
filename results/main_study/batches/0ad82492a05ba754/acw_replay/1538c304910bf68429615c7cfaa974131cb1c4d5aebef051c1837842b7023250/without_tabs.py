#!/usr/bin/env python3

try:
    cur = 0
    while True:
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        left = 0
        result = -1
        for i in range(n):
            if not a[i]:
                if k:
                    k -= 1
                else:
                    if result < i - left:
                        res_left = left
                        res_right = i
                        result = i - left
                    while i > left and a[left]:
                        left += 1
                    left += 1

        if i + 1 - left > result:
            res_left = left
            res_right = i + 1
            result = i + 1 - left

        print(result)
        for i in range(res_left):
            print(a[i], end=' ')
        for i in range(result):
            print(end="1 ")
        for i in range(res_right, n):
            print(a[i], end=' ')
        print()

except EOFError:
    pass
