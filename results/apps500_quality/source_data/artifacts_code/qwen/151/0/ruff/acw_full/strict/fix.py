import re


def fix_typos(word):
	vowels = 'aeiou'
	consonants = ''.join([c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in vowels])

	# Regular expression to find blocks of consonants with at least three different letters
	typo_pattern = r'(?=([bcdfghjklmnpqrstvwxyz]{2,}))[bcdfghjklmnpqrstvwxyz]{3,}'

	# Function to replace a typo with spaces
	def replace_typo(match):
		typo = match.group(0)
		blocks = re.findall(r'([bcdfghjklmnpqrstvwxyz]+)', typo)
		result = ' '.join(blocks)
		return result

	# Replace all typos in the word
	fixed_word = re.sub(typo_pattern, replace_typo, word)

	return fixed_word


# Read input from standard input
word = input().strip()

# Fix typos in the word
fixed_word = fix_typos(word)

# Print the fixed word
print(fixed_word)
