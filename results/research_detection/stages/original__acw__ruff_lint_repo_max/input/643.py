import re


def text_match_wordz_middle(text):
        patterns = '\Bz\B'
        return 'Found a match!' if re.search(patterns,  text) else 'Not matched!'