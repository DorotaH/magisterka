class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        strings = [s]

        if self.validate_string(s):
            return strings

        valid_string = False
        while not valid_string:
            results = []
            temp_strings = []
            for string in strings:
                for i, c in enumerate(string):
                    if c in ["(", ")"]:
                        temp_string = string[:i] + string[i+1:]
                        if self.validate_string(temp_string):
                            valid_string = True
                            if temp_string not in results:
                                results.append(temp_string)
                        else:
                            if temp_string not in temp_strings:
                                temp_strings.append(temp_string)
            if valid_string:
                return results
            strings = temp_strings

    def validate_string(self, s):
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
            elif c == ")":
                if cnt == 0:
                    return False
                else:
                    cnt -= 1
        return cnt == 0


