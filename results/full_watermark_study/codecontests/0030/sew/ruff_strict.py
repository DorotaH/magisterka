import sys

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    answer, n = 0, int(input())
    rhq, remain = n // 6, n % 6
    if not rhq == 0:
        answer = 15 * rhq
        if 0 < remain <= 2:
            answer += 5
        elif 2 < remain <= 4:
            answer += 10
        elif remain > 4:
            answer += 15
    else:
        answer = 15
    print(answer)
