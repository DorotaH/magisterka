import sys

n = int(sys.stdin.readline().strip())
volumes = list(map(int, sys.stdin.readline().split()))
temperatures = list(map(int, sys.stdin.readline().split()))

result = [0] * n
volumes = [(v, i) for i, v in enumerate(volumes)]
temperatures = [(t, i) for i, t in enumerate(temperatures)]

volumes.sort(key=lambda x: x[0])
temperatures.sort(key=lambda x: x[0])

i = 0
for t, _ in temperatures:
	while i < n and t >= volumes[i][0]:
		volumes[i] = (volumes[i][0] - t, volumes[i][1])
		i += 1

	result[volumes[i - 1][1]] = t

	for j in range(i, 0, -1):
		if temperatures[j][0] >= volumes[j - 1][0]:
			volumes[j - 1] = (volumes[j - 1][0] - temperatures[j][0], volumes[j - 1][1])

	i += 1

print(" ".join(map(str, result)))
