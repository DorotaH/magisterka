import  re
def text_match(text):
  patterns = '^[a-z]+_[a-z]+$'
  if not re.search(patterns,  text):
    return ('Not matched!')
  else:
    return ('Found a match!')
