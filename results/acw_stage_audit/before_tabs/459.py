import re


def remove_uppercase(str1):
  remove_upper = lambda text: re.sub('[A-Z]', '', text)
  return remove_upper(str1)
