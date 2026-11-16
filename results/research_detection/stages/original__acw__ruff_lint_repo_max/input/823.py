import re


def check_substring(string, sample): 
  if sample not in string:
    return ("entered string isnt a substring")
  y = "\A" + sample
  x = re.search(y, string)
  return ("string starts with the given substring"
          if x else "string doesnt start with the given substring")