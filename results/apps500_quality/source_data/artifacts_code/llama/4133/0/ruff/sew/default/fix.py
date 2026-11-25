import sys


def golorp(s):
    stack, max_depth = [], 0
    for c in s:
        if  c == '(':
            stack.append(c)
        elif  c == ')':
            stack.pop()
            if len(stack) == 0:
                max_depth = max_depth + 1
        elif  c in '-+*_/<>,':
            stack.append(c)
    if  stack or  (len(s) % 2 != 0):
        return  'false'

    depth, min_val = 0, ''
    for c in s:
        if  c == '(':
            min_val+='0'
        elif  c == '>':
            min_val+='1'
        elif  c == '<':
            min_val+='2'
        elif  c == '+':
            min_val+='3'
        elif  c == '/':
            min_val+='4'
        elif  c == '-':
            min_val+='5'
        elif  c == '*':
            min_val+='6'
        elif  c == ',':
            min_val+='7'
        else:
            min_val += '8'
        if  c == '(':
            depth = depth + 1
        if  c == ')':
            depth = depth - 1
        if  depth == max_depth:
            return min_val

    return min_val

s = sys.stdin.readline().strip()
print(golorp(s))