S = input()
N = len(S)

def get_three_consecutive_numbers(start):
    return int(S[start:start+3])

min_diff = float('inf')
for i in range(N - 2):
    diff = abs(get_three_consecutive_numbers(i) - 753)
    min_diff = min(min_diff, diff)

print(min_diff)
