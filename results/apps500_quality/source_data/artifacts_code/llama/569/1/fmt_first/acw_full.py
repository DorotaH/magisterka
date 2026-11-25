from collections import defaultdict


def min_changes(s):
	n = len(s)
	last_occ = {}
	changes = 0

	for i, c in enumerate(s):
		if c not in last_occ:
			last_occ[c] = [i]
		else:
			last_occ[c].append(i)

	for c in last_occ:
		for j in range(1, len(last_occ[c])):
			if last_occ[c][j] - last_occ[c][j - 1] == 1:
				changes += 1
				for k in range(last_occ[c][j - 1] + 1, last_occ[c][j]):
					s = (
						s[:k]
						+ chr((ord(s[k]) - ord("a") + 1) % 26 + ord("a"))
						+ s[k + 1 :]
					)
					last_occ = {}
					for i, c in enumerate(s):
						if c not in last_occ:
							last_occ[c] = [i]
						else:
							last_occ[c].append(i)
					for c in last_occ:
						for j in range(1, len(last_occ[c])):
							if last_occ[c][j] - last_occ[c][j - 1] == 1:
								changes += 1
								break
					if changes == -1:
						return -1

	return changes if changes != -1 else 0


n = int(input())
s = input().strip()
print(min_changes(s))
