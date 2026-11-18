class Solution:
    def countAndSay(self, n: int) -> str:
        def recursive(n):
            if n == 1:
                return '1'

            prev = recursive(n-1)
            count, curString = 1, []

            for i in range(len(prev)):
                if i == len(prev) - 1 or prev[i] != prev[i+1]:
                    curString.append(str(count))
                    curString.append(prev[i])
                    count = 1
                else:
                    count += 1

            return ''.join(curString)

        return recursive(n)
