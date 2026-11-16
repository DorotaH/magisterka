def  is_valid_parenthese( str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for  parenthese in  str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or  parenthese != pchar[stack.pop()]:
                return False
        return  0 == len(stack)