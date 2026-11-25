def is_mirror_word(word):
	mirror_map = {
		'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
		'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P',
		'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
		'Y': 'Y', 'Z': 'Z'
	}
	return next(
		(
			'NO'
			for i in range(len(word) // 2)
			if word[i] != mirror_map[word[-i - 1]]
		),
		'YES',
	)


# Read input from standard input
word = input().strip()

# Print the result
print(is_mirror_word(word))
