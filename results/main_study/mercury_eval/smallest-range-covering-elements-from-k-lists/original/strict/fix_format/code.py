class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # # find ls1 w smallest right
        # smallestRight, ls1 = None, None
        # for ls in nums:
        #     if smallestRight == None or ls[-1] < smallestRight:
        #         smallestRight, ls1 = ls[-1], ls

        # # find ls2 w largest left
        # largestLeft, ls2 = None, None
        # for ls in nums:
        #     if largestLeft == None or ls[0] > largestLeft:
        #         largestLeft, ls2 = ls[0], ls

        # # case A: l1 .... r1 .. l2 .... r2
        # # ret range [r1, l2]

        # # case B: l1 ... l2 .. r1 ... r2
        # # ret smallest range of [l1..., l2], subrange of [l2..., ...r1], [r1, ...r2]

        currMinHeap = [(nums[i][0], i, 0) for i in range(len(nums))]  # (val, ls, idx)
        heapq.heapify(currMinHeap)

        # currMaxHeap = [-ls[0] for ls in nums]
        # heapq.heapify(currMaxHeap)

        maxVal = max([ls[0] for ls in nums])

        ret, smallestRange = None, None

        while True:
            minVal, chosenList, chosenListIdx = heapq.heappop(currMinHeap)

            if smallestRange == None or maxVal - minVal < smallestRange:
                ret, smallestRange = [minVal, maxVal], maxVal - minVal

            if chosenListIdx < len(nums[chosenList]) - 1:
                heapq.heappush(
                    currMinHeap,
                    (
                        nums[chosenList][chosenListIdx + 1],
                        chosenList,
                        chosenListIdx + 1,
                    ),
                )
                maxVal = max(maxVal, nums[chosenList][chosenListIdx + 1])
            else:
                return ret

        # 4  0  5  [0, 5]
        # 4  9  5  [4, 9]
        # 10 9  5  [5, 10]
        # 10 9  18 [9, 18]
        # 10 12 18 [10, 18]
        # 15 12 18 [12, 18]
        # 15 20 18 [15, 20]
        # 24 20 18 [18, 24]
        # 24 20 22 [20, 24]

        # 24 20 30 [20, 30]
        # 26 20 30 [26, 30]
