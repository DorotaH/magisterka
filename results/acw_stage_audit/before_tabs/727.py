import re 


def remove_char(S):
  return re.sub('[\W_]+', '', S)
