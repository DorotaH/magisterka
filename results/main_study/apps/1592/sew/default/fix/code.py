
class Task:
    tasks, answer = [], "" 
	
    def getData(self):
        numberOfTasks = int(input())
        for i in range(numberOfTasks):
            self.tasks+=[[int(x) for  x in  input().split(' ')]]
        #inFile = open('input.txt', 'r')
        #inFile.readline().rstrip()
        #self.childs = inFile.readline().rstrip()

    def solve(self):
        queueSize, maxQueueSize = 0, 0
        time, timeOfLastMessage = 1, 1
        currentTask = 0
        while  currentTask<len(self.tasks) or  queueSize>0:
            maxQueueSize = max(maxQueueSize, queueSize)
            if not currentTask < len(self.tasks):
                timeOfLastMessage = time + queueSize
                break
            else:
                timeDelta = self.tasks[currentTask][0] - time
                queueSize -= min(queueSize, timeDelta)
                time += timeDelta
                
            if  currentTask<len(self.tasks) and  \
                    time == self.tasks[currentTask][0]:
                queueSize += self.tasks[currentTask][1]
                currentTask += 1
        self.answer = str(timeOfLastMessage) + " " + str(maxQueueSize)

    def printAnswer(self):
        print(self.answer)
        #outFile = open('output.txt', 'w')
        #outFile.write(self.answer)

task=Task()
task.getData()
task.solve()
task.printAnswer()