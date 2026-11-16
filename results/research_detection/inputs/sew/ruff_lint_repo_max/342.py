from heapq import heappop, heappush


class  Node:
    def __init__(self, value, list_num, index):
        self.value=value
        self.list_num=list_num
        self.index=index
    def __lt__(self, other):
        return self.value < other.value
def find_minimum_range(list):
    high, p = float('-inf'), (0, float('inf'))
    pq = []
    for  i in  range(0, len(list)):
        heappush(pq, Node(list[i][0], i, 0))
        high = max(high, list[i][0])
    while True:
        top=heappop(pq)
        low, i = top.value, top.list_num
        j=top.index
        if high - low < p[1] - p[0]:
            p=(low, high)
        if j == len(list[i]) - 1:
            return p
        heappush(pq, Node(list[i][1 + j], i, 1 + j))
        high=max(high, list[i][1 + j])
