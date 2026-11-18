#!/usr/bin/env python3
def main():
    M, K = map(int, input().split())
    if not K == 0:
        if K >= 2**M or M <= 1:
            print(-1)
        else:
            nums = []
            for i in range(2**M):
                if i != K:
                    nums.append(i)
            a = [nums[0], K, nums[0]]
            b = []
            for i in range(1, 2**M - 1):
                b.append(nums[i])
            b.append(K)
            for i in range(1, 2**M - 1):
                b.append(nums[2**M - 1 - i])
            print(*a, *b)
    else:
        print(*[i // 2 for i in range(2 ** (M + 1))])


def __starting_point():
    main()


__starting_point()
