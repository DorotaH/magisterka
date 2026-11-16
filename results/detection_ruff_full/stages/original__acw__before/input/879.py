import re
def text_match(text):
  patterns = 'a.*?b$'
  return 'Found a match!' if re.search(patterns,  text) else 'Not matched!'