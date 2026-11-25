def max_value(E, P, M):
    # Convert the expression to a list of numbers and operations
    tokens = []
    num = ""
    for char in E:
        if not char.isdigit():
            if num:
                tokens.append(int(num))
                num = ""
            tokens.append(char)
        else:
            num += char
    if num:
        tokens.append(int(num))

    # Function to evaluate the expression with given operations
    def evaluate(tokens, ops):
        stack, i = [], 0
        for token in tokens:
            if isinstance(token, int):
                stack.append(token)
            else:
                if token == "+":
                    stack.append(ops[i])
                elif token == "-":
                    stack.append(-ops[i])
                i += 1
        return eval(" ".join(map(str, stack)))

    # Generate all possible combinations of plus and minus operations
    from itertools import product

    max_val = float("-inf")
    for ops in product([1, -1], repeat=P + M):
        val = evaluate(tokens, ops)
        max_val = max(max_val, val)

    return max_val


# Read input
import sys

input = sys.stdin.read
data = input().split()
E = data[0]
P = int(data[1])
M = int(data[2])

# Output the result
print(max_value(E, P, M))
