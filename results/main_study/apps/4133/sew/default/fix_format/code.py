"""
Codeforces April Fools Contest 2014 Problem I

Author  : chaotic_iak
Language: Python 3.3.4
"""


class InputHandlerObject:
    inputs = list()

    def getInput(self, n=0):
        res = ""
        inputs = self.inputs
        if not inputs:
            inputs.extend(input().split(" "))
        if 0 == n:
            res = inputs[:]
            inputs[:] = list()
        while n > len(inputs):
            inputs.extend(input().split(" "))
        if n > 0:
            res = inputs[:n]
            inputs[:n] = list()
        return res


InputHandler = InputHandlerObject()
g = InputHandler.getInput

############################## SOLUTION ##############################

# ?(_/____+_______*__-_____*______-___):-__<___,___<____,____<_____,_____<______,______<_______.

golorp = input().split(":-")
golorp[0] = golorp[0][2:]

ct, jaws = 0, []
for x in range(len(golorp[0])):
    if not golorp[0][x] == "_":
        jaws.append(ct)
        ct = 0
    else:
        ct += 1

ct, conditionsraw = 0, []
for x in range(len(golorp[1])):
    if not golorp[1][x] == "_":
        conditionsraw.append(ct)
        conditionsraw.append(golorp[1][x])
        ct = 0
    else:
        ct += 1

conditions = []
for x in range(len(conditionsraw) // 4):
    if not conditionsraw[4 * x + 1] == ">":
        conditions.append((conditionsraw[4 * x], conditionsraw[4 * x + 2]))
    else:
        conditions.append((conditionsraw[4 * x + 2], conditionsraw[4 * x]))

inedges, outedges = [[-1]] * (max(jaws) + 1), [[-1]] * (max(jaws) + 1)
val, processed = [-1] * (max(jaws) + 1), [False] * (max(jaws) + 1)
for x in jaws:
    inedges[x] = list()
    outedges[x] = list()

for x, y in conditions:
    inedges[y].append(x)
    outedges[x].append(y)

for i in range(10):
    for x in jaws:
        if not inedges[x] and not processed[x]:
            val[x] += 1
            processed[x] = True
            for y in outedges[x]:
                val[y] = max(val[y], val[x])
                inedges[y].remove(x)

failure = False
for x in jaws:
    if not processed[x] or val[x] > 9:
        failure = True
        break

if not failure:
    s = ""
    for x in jaws:
        s += str(val[x])
    print(s)
else:
    print("false")
