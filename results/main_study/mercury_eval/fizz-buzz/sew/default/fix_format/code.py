class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, 1 + n):
            fizz = i % 3
            buzz = i % 5
            if 0 == fizz and 0 == buzz:
                res.append("FizzBuzz")
            elif 0 == fizz and 0 != buzz:
                res.append("Fizz")
            elif 0 != fizz and 0 == buzz:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
