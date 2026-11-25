import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))

student_dict = dict()
for i in range(n):
    student_dict.setdefault(s[i], []).append((p[i], i))

for school in student_dict:
    student_dict[school].sort(reverse=True)

ans = 0
for i in range(k):
    if student_dict[s[c[i] - 1][0][1]] != c[i] - 1:
        ans += 1

print(ans)
