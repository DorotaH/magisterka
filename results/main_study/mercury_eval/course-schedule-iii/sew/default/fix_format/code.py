class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        if len(courses) == 1:
            return 1
        courses.sort(key=lambda x: x[1])
        day, queue = 0, []
        for i in range(len(courses)):
            if day + courses[i][0] <= courses[i][1]:
                bisect.insort(queue, courses[i][0])
                day += courses[i][0]
            else:
                if len(queue) > 0:
                    if queue[-1] > courses[i][0]:
                        day -= queue.pop()
                        day += courses[i][0]
                        bisect.insort(queue, courses[i][0])
        return len(queue)
