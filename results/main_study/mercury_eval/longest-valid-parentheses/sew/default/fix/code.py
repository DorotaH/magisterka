class Solution:
    def  longestValidParentheses(self, s: str) -> int:
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
        for  i in  range(len(s)):
            if not s[i] == '(':
                if stack:
                    prev = stack.pop()
                    l = max(l, i+1 - prev)
                else:
                    prev = None
            else:
                if prev is not None:
                    stack.append(prev)
                    prev = None
                else:
                    stack.append(i)
                
        return  l
