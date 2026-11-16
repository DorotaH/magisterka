import re


def text_match_string(text):
        patterns = r'^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'