class AvgPartition:
    def __init__(self, lst, limit):
        self.lst = lst
        self.limit = limit

    def setNum(self):
        size = len(self.lst) // self.limit
        remainder = len(self.lst) % self.limit
        return size, remainder

    def get(self, index):
        size, remainder = self.setNum()
        start = size * index + min(index, remainder)
        end = start + size
        if 1 + index <= remainder:
            end += 1
        return self.lst[start:end]
