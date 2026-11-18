class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        if 0 == numRows:
            return final
        elif 1 == numRows:
            final.append([1])
            return final
        elif 2 == numRows:
            final.append([1])
            final.append([1, 1])
            return final
        else:
            final.append([1])
            final.append([1, 1])
            for i in range(1, numRows - 1):
                a = [1]
                jk = len(final[i][:]) - 1
                for ii in range(jk):
                    a.append(final[i][ii] + final[i][ii + 1])
                a.append(1)
                final.append(a)
            return final
