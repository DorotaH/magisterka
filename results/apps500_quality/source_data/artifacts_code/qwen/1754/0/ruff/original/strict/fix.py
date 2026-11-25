import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

powers = list(map(int, data[3:3+n]))
schools = list(map(int, data[3+n:3+2*n]))
chosen_ones = list(map(int, data[3+2*n:]))

# Sort students by their power in descending order
students = sorted(range(n), key=lambda i: powers[i], reverse=True)

# Dictionary to keep track of the strongest student in each school
strongest_in_school = {i: 0 for i in range(1, m+1)}
for student in students:
    if schools[student-1] not in strongest_in_school or powers[student-1] > powers[strongest_in_school[schools[student-1]]-1]:
        strongest_in_school[schools[student-1]] = student

# List of schools that need to be replaced
schools_to_replace = []

# Check which chosen ones are not the strongest in their schools
for chosen in chosen_ones:
    if chosen != strongest_in_school[schools[chosen-1]]:
        schools_to_replace.append(schools[chosen-1])

# Remove duplicates and sort the list of schools to replace
schools_to_replace = sorted(set(schools_to_replace))

# The minimal number of schools to be made up
print(len(schools_to_replace))
