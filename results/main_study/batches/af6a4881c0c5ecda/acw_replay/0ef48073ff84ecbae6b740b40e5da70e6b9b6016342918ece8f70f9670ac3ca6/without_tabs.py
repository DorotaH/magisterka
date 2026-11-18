class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            b = [[1], [1, 1]]
            x = 1
            while (rowIndex > x):
                a = b[x]
                s = [1]
                i = 0
                j = i + 1
                while (len(b[x]) > j):
                    c = 0
                    c = c + a[i] + a[j]
                    i = i + 1
                    j = 1 + j
                    s.append(c)
                s.append(1)
                b.append(s)
                x = 1 + x
        return b[rowIndex]
