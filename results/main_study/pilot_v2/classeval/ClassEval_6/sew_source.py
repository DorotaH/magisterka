class  AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        self.limit = limit

    def setNum(self):
        size, remainder = len(self.lst) // self.limit, len(self.lst) % self.limit
        return size, remainder

        
    def get(self, index):
        size, remainder = self.setNum()
        start = index * size + min(index, remainder)
        end = start + size
        if index + 1<=remainder:
            end = end + 1
        return self.lst[start:end]
