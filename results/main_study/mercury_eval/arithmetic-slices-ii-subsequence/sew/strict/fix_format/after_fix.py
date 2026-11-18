class  Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        # [7, 7, 7, 7, 7]
        # 2: 1 partial
        # 3: 1 complete, 1 + 2 = 3 partial
        # 4: 1 + 1 + 3 = 5 complete, 3 + 3 = 6 partial
        # 5: 5 + 5 + 6 = 16 complete, 6 + 5 = 11 partial

        partial = defaultdict(lambda: defaultdict(int)) # key: next number, value: {diff: num of sequences}
        complete = defaultdict(lambda: defaultdict(int)) # key: next number, value: {diff: num of sequences}
        num_slices = 0
        for  i in  range(1, len(nums)):
            n = nums[i]
            if n in complete:
                for  diff in  complete[n]:
                    num_slices += complete[n][diff]
                    complete[n + diff][diff] += complete[n][diff]
            if n in partial:
                for  diff in  partial[n]:
                    num_slices += partial[n][diff]
                    complete[n + diff][diff] += partial[n][diff]
            for  j in  range(i):
                diff = n - nums[j]
                partial[n + diff][diff] += 1

        return  num_slices
