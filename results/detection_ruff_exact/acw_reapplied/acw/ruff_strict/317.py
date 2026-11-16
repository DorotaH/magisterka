from itertools import groupby


def modified_encode(alist):
	def ctr_ele(el):
		return [len(el), el[0]] if 1 < len(el) else el[0]

	return [ctr_ele(list(group)) for key, group in groupby(alist)]
