n = int(input())
a = list(map(int, input().split()))
odd = []
even = []
for i in a:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
odd.sort()
even.sort()
if 1 >= abs(len(odd) - len(even)):
    print(0)
elif len(odd) > len(even):
    print(sum(odd[:len(odd) - len(even) - 1]))
else:
    print(sum(even[:len(even) - len(odd) - 1]))
