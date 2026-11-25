

def find_typos(word):
	vowels = 'aeiou'
	typos = []
	start = 0
	for i in range(len(word)):
		if word[i] not in vowels:
			if 2 < i - start and len(set(word[start:i])) > 1:
				typos.append((start, i))
			start = i
	if len(word) - start > 2 and len(set(word[start:])) > 1:
		typos.append((start, len(word)))
	return typos


def correct_typos(word):
	typos = find_typos(word)
	result = ''
	start = 0
	for typo in typos:
		result += ' ' + word[start:typo[0]]
		result += word[typo[0]:typo[1]] + ' '
		start = typo[1]
	result += word[start:]
	return result.strip()


word = input().strip()
print(correct_typos(word))
