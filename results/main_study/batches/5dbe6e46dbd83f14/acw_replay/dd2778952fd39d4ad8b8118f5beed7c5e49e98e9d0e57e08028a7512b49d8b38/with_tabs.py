class Solution:



	def containVirus(self, isInfected: List[List[int]]) -> int:
		"""
		I would start by mapping all the regions first, sorting them 
		by the number of walls needed to contain them.

		so we'll have build_a_wall(matrix) and I would mark that region then 
		with 2s, denoting it is contained.

		"""
		matrix = isInfected[:]
		m, n = len(matrix), len(matrix[0])

		def in_bounds(i, j):
			return 0 <= i < m and 0 <= j < n

		def infect(zone):
			# here we expand all the zones to the uninfected cells
			# visited = [[0 for _ in range(n)] for _ in range(m)]

			new_zone = zone.copy()
			walls = 0
			for i, j in zone:
				for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
					i2 = i + di
					j2 = dj + j
					if in_bounds(i2, j2) and (i2, j2) not in zone and matrix[i2][j2] == 0:
						new_zone.add((i2, j2))
						walls += 1

			return new_zone, walls

		def get_zones(matrix: List[List[int]]):

			zones = []

			virus = set()
			for i in range(m):
				for j in range(n):
					if matrix[i][j] == 1:
						virus.add((i, j))

			visited = set()

			while virus:
				# pick a random node
				ii, jj = virus.pop()
				if (ii, jj) in visited:
					continue

				q = deque([(ii, jj)])
				zone = set()

				# now deplete all the zone:
				while q:
					i, j = q.popleft()
					if (i, j) in zone:
						continue

					zone.add((i, j))

					for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
						i2 = i + di
						j2 = dj + j
						if in_bounds(i2, j2) and matrix[i2][j2] == 1:
							q.append((i2, j2))

				visited |= zone
				zones.append(zone.copy())

			return zones

		n_walls = 0

		zones = get_zones(matrix)
		if not zones:
			return 0

		while True:
			zones = get_zones(matrix)

			n_max_impact = -1
			max_impact_zone_index = None
			new_zones = []
			for i, zone in enumerate(zones):
				new_zone, walls = infect(zone)
				new_zones.append(new_zone)
				impact = len(new_zone) - len(zone)
				if n_max_impact < impact:
					max_impact_zone_index = i
					n_max_impact = impact
					new_walls = walls

			# contain with walls
			for (i, j) in zones[max_impact_zone_index]:
				matrix[i][j] = 2
			n_walls += new_walls

			# infect all other zones:
			zones = new_zones[:max_impact_zone_index] + new_zones[max_impact_zone_index + 1:]
			for zone in zones:
				for (i, j) in zone:
					matrix[i][j] = 1

			if not zones:
				return n_walls


