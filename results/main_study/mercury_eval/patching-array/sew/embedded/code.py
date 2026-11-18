class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += num
        counts = cur_max = i = 0
        while cur_max < n: 
            if  0 == len(hmap):
                cur_max += cur_max + 1
                counts += 1
            elif  i in hmap:
                cur_max = cur_max + hmap[i]
                hmap.pop(i)
            elif  i > cur_max:
                cur_max = cur_max + i
                counts = counts + 1              
            i += 1

        return counts    
