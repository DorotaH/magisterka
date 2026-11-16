def sector_area(r, a):
	pi = 22 / 7
	return None if a >= 360 else (r**2 * pi) * (a / 360)
