import  sys
import  math

n, q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

possible_values = [min(a), max(a)]

for  _ in  range(n - 1):
    new_values = []
    for  val1 in  possible_values:
        for  val2 in  possible_values:
            new_values.append((val1+val2)//2)
    possible_values = new_values

possible_values = sorted(set(possible_values))

q = int(sys.stdin.readline())
for  _ in  range(q):
    t = int(sys.stdin.readline())
    if t in possible_values:
        print("Yes")
    else:
        print("No")