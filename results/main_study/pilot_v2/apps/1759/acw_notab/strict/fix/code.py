"""
Codeforces Round 241 Div 1 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


class InputHandlerObject:
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
        if n > 0:
            res = inputs[:n]
            inputs[:n] = []
        return res


InputHandler = InputHandlerObject()
g = InputHandler.getInput

############################## SOLUTION ##############################
m, n = [int(x) for x in g()]
q = [[int(x) for x in g()] for _ in range(m)]
p = q[:]
for j in range(n):
    for i in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0:
            p[i][j] = q[i][j] + p[i][j - 1]
            continue
        if j == 0:
            p[i][j] = q[i][j] + p[i - 1][j]
            continue
        p[i][j] = q[i][j] + max(p[i - 1][j], p[i][j - 1])
for i in range(m):
    print(p[i][n - 1], end=" ")
