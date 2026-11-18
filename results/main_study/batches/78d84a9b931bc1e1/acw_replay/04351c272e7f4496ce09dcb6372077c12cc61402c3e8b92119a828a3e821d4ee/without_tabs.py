
class Task:
    tasks = []
    answer = ""

    def getData(self):
        numberOfTasks = int(input())
        for _ in range(0, numberOfTasks):
            self.tasks += [[int(x) for x in input().split(' ')]]
        #inFile = open('input.txt', 'r')
        #inFile.readline().rstrip()
        #self.childs = inFile.readline().rstrip()

    def solve(self):
        queueSize, maxQueueSize = 0, 0
        time, timeOfLastMessage = 1, 1
        currentTask = 0
        while len(self.tasks) > currentTask or 0 < queueSize:
            maxQueueSize = max(maxQueueSize, queueSize)
            if len(self.tasks) > currentTask:
                timeDelta = self.tasks[currentTask][0] - time
                queueSize -= min(queueSize, timeDelta)
                time += timeDelta
            else:
                timeOfLastMessage = queueSize + time
                break

            if len(self.tasks) > currentTask and \
                    self.tasks[currentTask][0] == time:
                queueSize += self.tasks[currentTask][1]
                currentTask += 1
        self.answer = str(timeOfLastMessage) + " " + str(maxQueueSize)

    def printAnswer(self):
        print(self.answer)
        #outFile = open('output.txt', 'w')
        #outFile.write(self.answer)


task = Task()
task.getData()
task.solve()
task.printAnswer()
