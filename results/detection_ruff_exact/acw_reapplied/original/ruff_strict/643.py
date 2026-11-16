import re


def text_match_wordz_middle(text):
	patterns = r"\Bz\B"
	return "Found a match!" if re.search(patterns, text) else "Not matched!"
