import re


def text_match(text):
  patterns = '^[a-z]+_[a-z]+$'
  return 'Found a match!' if re.search(patterns,  text) else 'Not matched!'