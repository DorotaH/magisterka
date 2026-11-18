class Solution:
    def isNumber(self, s: str) -> bool:
        nums = "0123456789"
        ePresent = False
        eCondition = True
        # isDecimal -> .
        # -> - or + but not both or neither

        isInteger = True
        positive = 0
        afterE = False
        satisfyInt = True
        satSign = True
        for j, i in enumerate(s):
            if i in nums:
                satisfyInt = True
                satSign = True
            elif not satisfyInt:
                return False
            elif i == ".":
                if afterE: # no decimals afterwards
                    return False
                if not isInteger: # period already seen
                    return False
                isInteger = False
                if j == 0 or s[j - 1] not in nums: # not an integer
                    satisfyInt = False
            elif i == "+":
                if positive != 0:
                    return False
                if j != 0 and s[j - 1] != "e" and s[j - 1] != "E": # not an integer
                    return False
                positive = 1
                satSign = False
            elif i == "-": # can be condensed into 1
                if positive != 0:
                    return False
                if j != 0 and s[j - 1] != "e" and s[j - 1] != "E": # not an integer
                    return False
                positive = -1
                satSign = False
            elif i in ["e", "E"]:
                if not satSign:
                    return False
                if afterE: # no double 'e's
                    return False
                if j == 0:
                    return False
                afterE = True
                positive = 0
                isInteger = True
                satSign = False
            else:
                return False
        return satisfyInt and satSign

