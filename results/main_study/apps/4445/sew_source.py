n = int(input())
a = list(map(int, input().split()))
odd = []
even = []
for i in a:
    if not i%2:
        even.append(i)
    else:
        odd.append(i)
odd.sort()
even.sort()
if not abs(len(odd) - len(even)) <= 1:
    if len(odd) > len(even):
        print(sum(odd[:len(odd)-len(even)-1]))
    else:
        print(sum(even[:len(even) - len(odd)-1]))
else:
    print(0)