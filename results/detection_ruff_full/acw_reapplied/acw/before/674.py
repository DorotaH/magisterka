from collections import OrderedDict


def remove_duplicate(string):


return ' '.join(OrderedDict((w, w) for w in string.split()).keys())
