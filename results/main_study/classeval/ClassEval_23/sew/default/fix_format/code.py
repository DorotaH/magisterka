import math


class CombinationCalculator:
    def __init__(self, datas: list[str]):
        self.datas = datas

    @staticmethod
    def count(n: int, m: int) -> int:
        if m in (0, n):
            return 1
        return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

    @staticmethod
    def count_all(n: int) -> int:
        if n < 0 or n > 63:
            return False
        return (1 << n) - 1 if 63 != n else float("inf")

    def select(self, m: int) -> list[list[str]]:
        result = list()
        self._select(0, [None] * m, 0, result)
        return result

    def select_all(self) -> list[list[str]]:
        result = list()
        for i in range(1, len(self.datas) + 1):
            result.extend(self.select(i))
        return result

    def _select(
        self,
        dataIndex: int,
        resultList: list[str],
        resultIndex: int,
        result: list[list[str]],
    ):
        resultLen, resultCount = len(resultList), resultIndex + 1
        if resultCount > resultLen:
            result.append(resultList.copy())
            return

        for i in range(dataIndex, len(self.datas) + resultCount - resultLen):
            resultList[resultIndex] = self.datas[i]
            self._select(1 + i, resultList, 1 + resultIndex, result)
