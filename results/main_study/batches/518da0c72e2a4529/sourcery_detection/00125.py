class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ''' Ideas:
        1. Same number of ( and )
        2. ( is to the left of )
        3. Stack data structure to verify
        4. Must be an even length

        Stack will hold the index of the (
        When the ) arrives, we can calculate the distance to its (
        '''
        l = 0
        stack = []
        prev = None
        for i in range(len(s)):
            if s[i] == '(':
                if prev is None:
                    stack.append(i)
                else:
                    stack.append(prev)
                    prev = None
            elif stack:
                prev = stack.pop()
                l = max(l, i+1 - prev)
            else:
                prev = None

        return l