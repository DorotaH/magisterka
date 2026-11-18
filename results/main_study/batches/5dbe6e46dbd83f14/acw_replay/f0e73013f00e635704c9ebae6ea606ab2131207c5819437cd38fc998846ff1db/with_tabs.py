class Solution:
	def getLettersCount(s):
		d = {}
		for c in s:
			if not c in d:
				d[c] = 0
			d[c] += 1
		return d

	def updateAndDelIfZero(self, d, k, valBy):
		if not k in d:
			d[k] = 0
		d[k] += valBy
		if d[k] == 0:
			del d[k]

	def allNonPos(self, d):
		return all(0 >= v for k, v in d.items())

	def moveForward(self, s, start, lettersNeeded, lettersSet):
		missing = 0
		while start < len(s):
			c = s[start]
			if c in lettersSet:
				if not c in lettersNeeded:
					missing += 1
				# don't remove, but begin from here
				if missing == 1:
					return start
				self.updateAndDelIfZero(lettersNeeded, c, 1)
			start += 1
		return start

	def minWindow(self, s: str, t: str) -> str:

		if len(t) > len(s):
			return ""

		lettersSet = set()
		lettersNeeded = {}
		for c in t:
			self.updateAndDelIfZero(lettersNeeded, c, 1)
			lettersSet.add(c)
		# 01234567890123
		# ADOBBECODEBANC   ABC    r: BANC
		# a 0
		# b -1
		# c 0

		start = 0
		end = start
		shortestSubstr = None
		while len(s) > end:
			c = s[end]
			if s[end] in lettersSet:
				self.updateAndDelIfZero(lettersNeeded, c, -1)
				if self.allNonPos(lettersNeeded):
					# reduce substring just before we need to remove needed letter
					start = self.moveForward(s, start, lettersNeeded, lettersSet)
					if (
						shortestSubstr is None
						or shortestSubstr[1] - shortestSubstr[0] > end - start
					):
						shortestSubstr = (start, end)
					# move forward just before we need a new letter (but stop before)
					start = self.moveForward(s, start, lettersNeeded, lettersSet)
			end += 1

		if shortestSubstr is None:
			return ""
		return s[shortestSubstr[0] : 1 + shortestSubstr[1]]
