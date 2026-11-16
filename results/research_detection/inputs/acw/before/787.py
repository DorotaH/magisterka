import re


def text_match_three(text):
		patterns = 'ab{3}?'
		return 'Found a match!' if re.search(patterns, text) else 'Not matched!'
