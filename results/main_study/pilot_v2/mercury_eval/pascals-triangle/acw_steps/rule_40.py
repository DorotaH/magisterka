class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        if numRows == 0:
            return final
        elif numRows == 1:
            final.append([1])
            return final
        elif numRows == 2:
            final.extend(([1], [1, 1]))
            return final
        else:
            final.extend(([1], [1, 1]))
            for i in range(1, numRows - 1):
                a = [1]
                jk = len(final[i][:]) - 1
                for ii in range(jk):
                    a.append(final[i][ii] + final[i][1 + ii])
                a.append(1)
                final.append(a)
            return final

        