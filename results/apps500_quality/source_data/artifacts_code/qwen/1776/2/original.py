import sys
from typing import List

def evaluate_expression(expression: str, operators: List[str]) -> int:
    stack = []
    i = 0
    j = 0
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            temp = 0
            while stack[-1] != '(':
                temp += stack.pop()
            stack.pop()  # Remove '('
            if stack and stack[-1] in operators:
                op = stack.pop()
                if op == '+':
                    temp = temp + stack.pop()
                else:
                    temp = stack.pop() - temp
            stack.append(temp)
        elif char.isdigit():
            stack.append(int(char))
        elif char in operators:
            if j < len(operators):
                stack.append(operators[j])
                j += 1
    return stack[0]

def main():
    input = sys.stdin.read
    data = input().split()
    expression = data[0]
    P, M = map(int, data[1:])
    operators = ['+'] * P + ['-'] * M
    result = evaluate_expression(expression, operators)
    print(result)

if __name__ == "__main__":
    main()
