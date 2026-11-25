import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))

student_dict = {}
for i in range(n):
    student_dict.setdefault(s[i], []).append((p[i], i))

for school, value in student_dict.items():
    value.sort(reverse=True)

ans = sum(bool(student_dict[s[c[i] - 1][0][1]] != c[i] - 1)
      for i in range(k))
print(ans)
