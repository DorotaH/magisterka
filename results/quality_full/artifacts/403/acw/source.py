import re


def is_valid_URL(str):
	regex = ("[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"((http|https)://)(www.)?" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")
	p = re.compile(regex)
	return False if (str == None) else bool((re.search(p, str)))
