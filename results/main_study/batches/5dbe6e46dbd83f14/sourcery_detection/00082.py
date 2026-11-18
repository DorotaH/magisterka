class Solution:
    def grayCode(self, n: int) -> List[int]:
        gc_list = self.grayCodeList(n)
        return [ self.decimal(gc_bin) for gc_bin in gc_list ]

    def grayCodeList(self,n: int) -> List[List[int]]:
        if n == 1:
            return [[0],[1]]
        gc_part = self.grayCodeList(n-1)
        gc1 = [ code + [0] for code in gc_part ]
        gc_part.reverse()
        gc2 = [ code + [1] for code in gc_part ]
        return gc1 + gc2

    def decimal(self, b : List[int]) -> int:
        return sum((2**i)*b[i] for i in range(len(b)))
        