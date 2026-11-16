import re


def text_lowercase_underscore(text):
		patterns = '^[a-z]+_[a-z]+$'
		return 'Found a match!' if re.search(patterns, text) else 'Not matched!'
