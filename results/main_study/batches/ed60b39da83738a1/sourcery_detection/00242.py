class Solution:
    def isValid(self, s: str) -> bool:
        openings = "({["
        closings = ")}]"
        stack = []
        for char in s:
            # print("char: ", char, " stack: ", stack)
            if char in openings:
                # print("opening")
                stack.append(char)
            if char in closings:
                # print("closing")
                if not stack:
                    # print("len == 0")
                    return False
                if closings.index(char) != openings.index(stack[-1]):
                    # print("closings index: ", closings.index(char), "openings.index: ", openings.index(stack[-1]))
                    return False
                stack.pop()
        if stack:
            return False
        return True