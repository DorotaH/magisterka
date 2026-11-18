class Solution:
	def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
		freq = {}
		minx1 =  float('inf')
		miny1 =  float('inf')
		maxx2 =  float('-inf')
		maxy2 =  float('-inf')
		res = 0
		for x1, y1, x2, y2 in rectangles:
			p1 = (x1, y1)
			p2 = (x2, y2)
			p3 = (x1, y2)
			p4 = (x2, y1)
			freq[p1] = 1 + freq.get(p1, 0)
			freq[p2] = 1 + freq.get(p2, 0)
			freq[p3] = freq.get(p3, 0) + 1
			freq[p4] = freq.get(p4, 0) + 1
			area = (x2 - x1) * (y2 - y1)
			res += area
			if x1 <= minx1 and miny1 >= y1:
				minx1 = x1
				miny1 = y1 
			if maxx2 <= x2 and y2 >= maxy2:
				maxx2 = x2
				maxy2 = y2 

		points = [k for k, v in freq.items() if v % 2 == 1]
		if len(points) != 4:
			return False
		# else:
		#     for p in points:
		#         if freq[p] != 1:
		#             return False

		largetRec = (maxx2 - minx1) * (maxy2 - miny1)
		if largetRec != res:
			return False 

		return all(
			p in [(minx1, miny1), (maxx2, maxy2), (minx1, maxy2), (maxx2, miny1)]
			for p in points
		)







