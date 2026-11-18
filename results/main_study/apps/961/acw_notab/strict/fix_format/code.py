def dp():
    dparr = [0] * len(sections)
    for i in range(len(sections) - 1, -1, -1):
        _, curend, curcomfort = sections[i]
        nextsection = i + 1
        try:
            while curend >= sections[nextsection][0]:
                nextsection += 1
        except IndexError:
            # Loop til end
            inc = curcomfort
        else:
            inc = dparr[nextsection] + curcomfort
        exc = 0 if i == len(sections) - 1 else dparr[i + 1]
        dparr[i] = max(inc, exc)
    return dparr[0]


n = int(input())
zs = list(map(int, input().split()))
sections = []
seenstartz = set()
first = {z: i for i, z in reversed(list(enumerate(zs)))}
last = {z: i for i, z in enumerate(zs)}
for start, z in enumerate(zs):
    if z in seenstartz:
        continue
    seenstartz.add(z)
    end = last[z]
    comfort = 0
    i = start
    while i <= end:
        if start > first[zs[i]]:
            break
        if i == last[zs[i]]:
            comfort ^= zs[i]
        end = max(end, last[zs[i]])
        i += 1
    else:
        sections.append((start, end, comfort))

ans = dp()
print(ans)
