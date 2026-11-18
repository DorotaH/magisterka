
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        tmp = []        
        
        while intervals and intervals[-1][0] > newInterval[0]:
            tmp.append(intervals.pop())
        
        tmp.append(newInterval)
        while tmp:
            top = tmp.pop()
            elem = top
            if intervals:
                if intervals[-1][1] < top[0]:
                    elem = top
                else:
                    old = intervals.pop()
                    elem = [old[0], max(old[1], top[1])]

            intervals.append(elem)
        return intervals