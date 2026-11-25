def process_slimes(n):
    slimes = [1]
    for _ in range(1, n):
        slimes.append(slimes[-1])
        while len(slimes) >= 2 and slimes[-2] == slimes[-1]:
            slimes.pop()
            slimes[-1] += 1
    return slimes


n = int(input())
result = process_slimes(n)
print(" ".join(map(str, result)))
