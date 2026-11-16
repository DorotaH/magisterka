def is_valid_parenthese( str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
                if parenthese in pchar:
                        stack.append(parenthese)
                elif not stack or pchar[stack.pop()] != parenthese:
                        return False
        return not stack