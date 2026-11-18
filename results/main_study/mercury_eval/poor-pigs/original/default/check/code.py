class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        memo = dict()
        experiments = minutesToTest // minutesToDie
        # iterate through each number of pigs 1, 2, ... (each time need pascal's triangle)
        # 0 = [0:1]
        # 1 = [0:1, 1:1]
        # 2 = [0:1, 1:2, 2:1]
        pigs = 0
        pascal = {0:[1]}
        while True:
            max_buckets = self.recSolver(pigs, experiments, memo, pascal)
            if buckets <= max_buckets:
                return pigs
            
            # for pigs = k, recursively compute for each pig count: 
            # pascal[count] * sol(count, exp-1)
            # keep memo that tracks solutions for sol(c, t)

            new_level = [1]
            for i in range(len(pascal[pigs]) - 1):
                new_level.append(pascal[pigs][i] + pascal[pigs][i+1])
            new_level.append(1)
            pigs += 1
            pascal[pigs] = new_level
        
        return -1
    
    def recSolver(self, pigs, trials, memo, pascal):
        if (pigs, trials) in memo:
            return memo[(pigs, trials)]

        if pigs == 0 or trials == 0:
            return 1
        
        pascal_row = pascal[pigs]
        buckets = 0
        for pigs_left in range(len(pascal_row)):
            buckets += pascal_row[pigs_left] * self.recSolver(pigs_left, trials - 1, memo, pascal)
        
        memo[(pigs, trials)] = buckets
        return buckets



