"""
Codeforces Round 240 Div 1 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""

class InputHandlerObject(object):
    inputs = []

    def getInput(self, n=0):
        res = ""
        inputs = self.inputs
        if not inputs: inputs.extend(input().split(" "))
        if n == 0:
            res = inputs[:]
            inputs[:] = []
        while len(inputs) < n:
            inputs.extend(input().split(" "))
        if 0 < n:
            res = inputs[:n]
            inputs[:n] = []
        return res
InputHandler = InputHandlerObject()
g = InputHandler.getInput

############################## SOLUTION ##############################
n, a, b = g()
n, a, b = int(n), int(a), int(b)
c = [int(x) for x in g()]
r = [str(((i * a) % b) // a) for i in c]
print(" ".join(r))
