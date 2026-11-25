import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

# If there's only one zombie, Heidi can take the only brain
if N == 1:
	print(1)
else:
	# For more than one zombie, Heidi needs to offer herself one brain and the rest to the lowest-ranked zombie
	# to ensure she gets at least one brain and the vote of the lowest-ranked zombie
	print(2)
