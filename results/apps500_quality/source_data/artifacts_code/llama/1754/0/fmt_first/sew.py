from collections import defaultdict
import sys

def solve():
    n, m, k = map(int, input().split())
    p, s = list(map(int, input().split())), list(map(int, input().split()))
    c = list(map(int, input().split()))

    student_by_school = defaultdict(list)
    for  i in  range(n):
        student_by_school[s[i]].append((p[i], i))

    made_up_schools = 0
    for  student_id in  c:
        student = student_by_school[s[student_id - 1]]
        max_power = max(student)
        if  max_power[0] != student_id:
            made_up_schools = made_up_schools + 1
            del student_by_school[s[student_id - 1]]
            student_by_school[str(m+made_up_schools)]=[(max_power[0], max_power[1])]

    return  made_up_schools


input_lines = sys.stdin.read().splitlines()
n, m, k = map(int, input_lines[0].split())
p, s = list(map(int, input_lines[1].split())), list(map(int, input_lines[2].split()))
c = list(map(int, input_lines[3].split()))

print(solve())
