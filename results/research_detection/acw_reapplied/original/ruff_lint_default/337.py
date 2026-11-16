import re


def text_match_word(text):
		patterns = r'\w+\S*$'
		return 'Found a match!' if re.search(patterns, text) else 'Not matched!'
