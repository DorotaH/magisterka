import re


def text_match(text):
        patterns = 'ab*?'
        if not re.search(patterns,  text):
                return('Not matched!')
        else:
                return 'Found a match!'
