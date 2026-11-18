

class Task:
    maxDigitSum = 18 * 9
    n = 0
    answer = "" 
	
    def getData(self):
        self.n = int(input())
        #inFile = open('input.txt', 'r')
        #inFile.readline().rstrip()
        #self.childs = inFile.readline().rstrip()

    def solve(self):
        if self.n == 1:
            self.answer = '-1'
            return

        xL, xR = 0, self.n
        while xL + self.maxDigitSum < xR:
            xM = (xL + xR) // 2
            if xM**2 + xM * self.digitSum(xM) < self.n:
                for x in range(xM - 1, max(xL, xM - self.maxDigitSum) - 1, -1):
                    if x**2 + self.digitSum(x) * x == self.n:
                        self.answer = x
                        return
                xL = xM
            else:
                for x in range(xM + 1, min(xR, self.maxDigitSum + xM) + 1):
                    if x**2 + self.digitSum(x) * x == self.n:
                        self.answer = x
                        return
                xR = xM
        for x in range(xL, 1 + xR):
            if x**2 + self.digitSum(x) * x == self.n:
                self.answer = x
                return
        self.answer = -1

    def digitSum(self, n):
        return sum(int(x) for x in str(n))

    def printAnswer(self):
        print(self.answer)
        #outFile = open('output.txt', 'w')
        #outFile.write(self.answer)


task = Task()
task.getData()
task.solve()
task.printAnswer()
