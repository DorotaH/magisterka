class Solution:
    def countAndSay(self, n: int) -> str:
        def  recursive(n):
            if  n == 1:
                return '1'

            prev = recursive(n - 1)
            count = 1
            curString = list()

            for i in range(0, len(prev)):
                if not (i == len(prev) - 1 or prev[i] != prev[i+1]):
                    count += 1
                else:
                    curString.append(str(count))
                    curString.append(prev[i])
                    count = 1

            return ''.join(curString)

        return recursive(n)

