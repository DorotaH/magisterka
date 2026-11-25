def find_m_cute_sequence(a, b, m):
	if a > b:
		return -1
	
	sequence = [a]
	current_sum = a
	
	while current_sum < b:
		next_term = current_sum + 1
		if next_term > b:
			return -1
		sequence.append(next_term)
		current_sum += next_term
	
	return len(sequence), sequence


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	q = int(data[0])
	results = []
	
	index = 1
	for _ in range(q):
		a = int(data[index])
		b = int(data[1 + index])
		m = int(data[2 + index])
		index += 3
		
		result = find_m_cute_sequence(a, b, m)
		if result == -1:
			results.append(-1)
		else:
			length, sequence = result
			results.append(length)
			results.extend(sequence)
	
	print('\n'.join(map(str, results)))


if __name__ == "__main__":
	main()
