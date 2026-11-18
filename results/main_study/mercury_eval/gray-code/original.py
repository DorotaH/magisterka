class Solution:
    def grayCode(self, n: int) -> List[int]:
        gc_list = self.grayCodeList(n)
        gc = [ self.decimal(gc_bin) for gc_bin in gc_list ]
        return gc

    def grayCodeList(self,n: int) -> List[List[int]]:
        if n == 1:
            return [[0],[1]]
        else:
            gc_part = self.grayCodeList(n-1)
            gc1 = [ code + [0] for code in gc_part ]
            gc_part.reverse()
            gc2 = [ code + [1] for code in gc_part ]
            gc = gc1 + gc2
            return gc

    def decimal(self, b : List[int]) -> int:
        dec = 0
        for i in range(0,len(b)):
            dec += (2**i)*b[i]
        return dec
        