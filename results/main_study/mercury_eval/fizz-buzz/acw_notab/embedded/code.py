class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = list()
        for i in range(1, 1 + n):
            fizz = i % 3
            buzz = i % 5
            if fizz == 0 and buzz == 0:
                res.append('FizzBuzz')
            elif fizz == 0:
                res.append('Fizz')
            elif buzz == 0:
                res.append('Buzz')
            else: 
                res.append(str(i))
        return res
