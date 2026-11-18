OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b),
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > i:
            c = tokens[i]
            if c not in OPS:
                i += 1
                continue
            
            tokens[i - 2 : i + 1] = [OPS[c](int(tokens[i - 2]), int(tokens[i - 1]))]
            i -= 1

        return int(tokens[0])