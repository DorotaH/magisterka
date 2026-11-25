import sys

s = input()

# replace 3+ with 3, 2+ with 2, 1+ with 1
s = s.replace("3+", "3").replace("2+", "2").replace("1+", "1")

# remove '+' from the string
s = s.replace("+", "")

# sort the string
s = "".join(sorted(s))

# add '+' between every two characters
s = "+".join([c for c in s])

print(s)
