import re


def check_literals(text, patterns):
  for pattern in patterns:
    return 'Matched!' if re.search(pattern, text) else 'Not Matched!'
