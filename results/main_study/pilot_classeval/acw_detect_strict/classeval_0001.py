import math


class AreaCalculator:
	def __init__(self, radius):
		self.radius = radius

	def calculate_circle_area(self):
		return math.pi * self.radius**2

	def calculate_sphere_area(self):
		return math.pi * 4 * self.radius**2

	def calculate_cylinder_area(self, height):
		return 2 * math.pi * self.radius * (self.radius + height)

	def calculate_sector_area(self, angle):
		return angle * self.radius**2 / 2

	def calculate_annulus_area(self, inner_radius, outer_radius):
		return (outer_radius**2 - inner_radius**2) * math.pi
