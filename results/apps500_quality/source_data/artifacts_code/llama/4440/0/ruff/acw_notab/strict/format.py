import math

L = float(input())

# We are looking for the maximum volume of a rectangular cuboid
# whose sum of the dimensions is L.
# The maximum volume will be achieved when the three dimensions are as close to each other as possible.
# Therefore, we divide L by 3 to get the maximum value of each dimension.

max_dim = L / 3
# Since the maximum possible dimensions should be as close to each other as possible,
# we take the cube root of the result from the previous step.
max_dim = round(math.pow(max_dim, 1 / 3), 6)

# Now we can calculate the maximum volume.
volume = max_dim * max_dim * max_dim

print(volume)
