def palindrome_lambda(texts):
return list(filter(lambda x: (x == "".join(reversed(x))), texts))
