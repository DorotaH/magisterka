#!/usr/bin/env python3

try:
    while True:
        n, k = map(int, input().split())
        a, left = list(map(int, input().split())), 0
        result, cur = -1, 0
        for i in range(n):
            if not a[i]:
                if not k:
                    if i - left > result:
                        res_left = left
                        res_right = i
                        result = i - left
                    while left < i and a[left]:
                        left += 1
                    left += 1
                else:
                    k -= 1

        if 1 + i-left>result:
            res_left=left
            res_right, result = i + 1, i + 1 - left

        print(result)
        for i in range(res_left):
            print(a[i], end=' ')
        for i in range(result):
            print(end="1 ")
        for i in range(res_right, n):
            print(a[i], end=' ')
        print()

except  EOFError:
    ...
