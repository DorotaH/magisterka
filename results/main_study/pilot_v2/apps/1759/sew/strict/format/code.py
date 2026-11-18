"""
Codeforces Round 241 Div 1 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


class InputHandlerObject(object):
    inputs = []

    def getInput(self, n=0):
        res = ""
        inputs = self.inputs
        if not inputs:
            inputs.extend(input().split(" "))
        if 0 == n:
            res = inputs[:]
            inputs[:] = []
        while n > len(inputs):
            inputs.extend(input().split(" "))
        if n > 0:
            res = inputs[:n]
            inputs[:n] = []
        return res


InputHandler = InputHandlerObject()
g = InputHandler.getInput

############################## SOLUTION ##############################
m, n = [int(x) for x in g()]
q = []
for i in range(0, m):
    q.append([int(x) for x in g()])
p = q[:]
for j in range(0, n):
    for i in range(m):
        if 0 == i and 0 == j:
            continue
        if 0 == i:
            p[i][j] = p[i][j - 1] + q[i][j]
            continue
        if 0 == j:
            p[i][j] = p[i - 1][j] + q[i][j]
            continue
        p[i][j] = max(p[i - 1][j], p[i][j - 1]) + q[i][j]
for i in range(0, m):
    print(p[i][n - 1], end=" ")
