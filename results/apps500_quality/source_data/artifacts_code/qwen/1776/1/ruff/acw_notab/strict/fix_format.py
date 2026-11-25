def evaluate_expression(expression, plus_count, minus_count):
    def dfs(expression):
        if expression.isdigit():
            return int(expression)
        stack = []
        i = 0
        while len(expression) > i:
            if expression[i].isdigit():
                j = i
                while len(expression) > j and expression[j].isdigit():
                    j += 1
                stack.append(dfs(expression[i:j]))
                i = j
            elif expression[i] == "(":
                j = i
                count = 1
                while count > 0:
                    j += 1
                    if expression[j] == "(":
                        count += 1
                    elif expression[j] == ")":
                        count -= 1
                stack.append(dfs(expression[i + 1 : j]))
                i = 1 + j
            elif expression[i] in "+-":
                op = expression[i]
                i += 1
                j = i
                while len(expression) > j and expression[j].isdigit():
                    j += 1
                if op == "+":
                    stack.append(int(expression[i:j]))
                elif op == "-":
                    stack.append(-int(expression[i:j]))
                i = j
        result = stack[0]
        for j in range(1, len(stack), 2):
            result += stack[j] if stack[j] > 0 else stack[j]
        return result

    # Replace '?' with '+' and '-' based on the counts
    expression = expression.replace("?", "+")
    result = dfs(expression)
    expression = expression.replace("+", "?")
    expression = expression.replace("-", "?")
    expression = expression.replace("?", "-")
    result = dfs(expression)
    return result


# Read input
import sys

input = sys.stdin.read
data = input().split()
expression = data[0]
plus_count = int(data[1])
minus_count = int(data[2])

# Output the result
print(evaluate_expression(expression, plus_count, minus_count))
