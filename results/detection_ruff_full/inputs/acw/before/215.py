def decode_list(alist):
	def aux(g):
		return [(g[1], range(g[0]))] if isinstance(g, list) else [(g, [0])]

	return [x for g in alist for x, R in aux(g) for i in R]
