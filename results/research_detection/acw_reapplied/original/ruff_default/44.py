import re


def text_match_string(text):
	patterns = "^\w+"
	return "Found a match!" if re.search(patterns, text) else "Not matched!"
