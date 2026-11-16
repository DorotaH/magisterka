import re


def string_literals(patterns, text):
	for pattern in patterns:
		return "Matched!" if re.search(pattern, text) else "Not Matched!"
