import numpy as np


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n, x = len(gas), []
        for i in range(n):
            x.append(gas[i] - cost[i])

        print(x)

        rt, cnt = [], 0
        for i in range(n):
            cnt = cnt + x[i]
            rt.append(cnt)

        rt = np.array(rt)

        sum_v = sum(x, 0)
        if sum_v < 0:
            return -1

        index, min_v = 0, min(rt)
        while True:
            # print(index)
            # print(rt)
            # print('min',min_v)
            if min_v >= 0:
                return index
            if index == n - 1:
                break
            # print('x', x[index])
            # rt[:n-1] = rt[1:n]-x[index]
            # rt[n-1] = rt[n-2] + x[index]
            min_v = min(min_v - x[index], sum_v)
            index = index + 1

        return -1

        # for i in range(n):
        #     if x[i] < 0:
        #         continue
        #     total_sum = 0
        #     cnt = i
        #     while True:
        #         total_sum += x[cnt]
        #         if total_sum < 0:
        #             break
        #         if cnt == (i-1)%n:
        #             return i
        #         cnt = (cnt+1)%n

        return -1
