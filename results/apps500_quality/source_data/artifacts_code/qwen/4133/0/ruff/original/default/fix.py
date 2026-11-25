import sys


def feed_golorp(golorp_name):
    # Parse the golorp name to determine the shape of its jaws and the operations
    jaws = []
    stack = []
    for char in golorp_name:
        if char.isdigit():
            stack.append(int(char))
        elif char == '?':
            stack = []
        elif char == '-':
            stack.append(-stack.pop())
        elif char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        elif char == '/':
            b = stack.pop()
            a = stack.pop()
            if b == 0:
                return "false"
            stack.append(a // b)
        elif char == '<':
            jaws.append(stack.pop())
        elif char == '>':
            stack.append(jaws.pop())
    return ''.join(map(str, stack)) if not jaws else "false"

# Read the input from standard input
golorp_name = sys.stdin.read().strip()

# Print the result
print(feed_golorp(golorp_name))
