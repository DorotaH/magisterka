class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for building in buildings:
            events.append((building[0],building[2],1))
            events.append((building[1],building[2],-1))
        
        events.sort(key=lambda x: (x[0],x[1]) if x[2]==-1 else (x[0],-x[1]))
        heap = [0]  
        res = []
        for event in events:
            if event[2] == 1:
                if event[1]>-heap[0]:
                    res.append([event[0],event[1]])
                heapq.heappush(heap,-event[1])
                    
            if event[2] == -1:

                heap.remove(-event[1])
                heapq.heapify(heap)
                if event[1] > -heap[0]:
                    res.append([event[0],-heap[0]])
        return res
