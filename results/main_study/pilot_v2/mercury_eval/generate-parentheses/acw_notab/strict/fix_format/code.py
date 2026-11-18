class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                answer = "".join(stack)
                res.append(answer)

            if openN > closeN:
                stack.append(")")
                backtrack(openN, 1 + closeN)
                stack.pop()

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

        backtrack(0, 0)
        return res
