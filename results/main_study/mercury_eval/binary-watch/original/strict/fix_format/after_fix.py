class Solution:
    def countBits(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        result = []
        for hour in range(12):
            for minute in range(60):
                if self.countBits(hour) + self.countBits(minute) == turnedOn:
                    temp = f'{hour}:{minute:02d}'
                    result.append(temp)

        return result
