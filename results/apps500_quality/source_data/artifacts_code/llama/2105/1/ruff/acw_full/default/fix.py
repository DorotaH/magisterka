

def gapja(n, m, s, t):
	# Create a dictionary to store unique strings from s and t
	s_set = set(s)
	t_set = set(t)
	all_set = s_set.union(t_set)
	
	# Initialize the result list and the index pointers
	res = []
	si, ti = 0, 0
	
	# Find the minimum length of the cycles
	cycle_len = max(len(s), len(t))
	
	# Simulate the Gapja system
	for i in range(1, 2021):
		# If the current year is a multiple of the cycle length, start a new cycle
		if i % cycle_len == 1:
			si = 0
			ti = 0
		
		# Concatenate the next strings from s and t
		res.append(s[si] + t[ti])
		
		# Move the index pointers
		si = (si + 1) % len(s)
		ti = (ti + 1) % len(t)
	
	# Create a dictionary to store the year and its corresponding name
	year_name = {}
	for i in range(cycle_len):
		year_name[i + 1] = res[i]
	
	# Return the names for the given years
	return '\n'.join([year_name.get(i, 'Unknown') for i in map(int, input().split())])


# Read the input
n, m = map(int, input().split())
s = input().split()
t = input().split()

# Get the number of queries
q = int(input())

# Print the results
print(gapja(n, m, s, t))
