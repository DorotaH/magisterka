class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (0 > numerator) != (0 > denominator):
            s.append("-")

        # 整数部分
        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.extend((str(integerPart), "."))
        # 小数部分
        indexMap = {}
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:  # 有循环节
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, "(")
            s.append(")")

        return "".join(s)
