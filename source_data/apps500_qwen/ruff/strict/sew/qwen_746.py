n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools, chosen_ones = list(map(int, input().split())), list(map(int, input().split()))

# Create a list of tuples (power, school) and sort it by power in descending order
students = sorted(zip(powers, schools), reverse=True)

# Create a list to keep track of the strongest student in each school
strongest_in_school = [0] * (m + 1)
for power, school in students:
    if power > strongest_in_school[school]:
        strongest_in_school[school] = power

# Create a list of students who are not Chosen Ones but are the strongest in their school
not_chosen = [
    i
    for i in range(0, n)
    if i + 1 not in chosen_ones and powers[i] == strongest_in_school[schools[i]]
]

# Sort the not_chosen list by power in descending order
not_chosen.sort(key=lambda i: powers[i], reverse=True)

# Create a list to keep track of the schools that have been made up
made_up_schools = set()

# Iterate over the not_chosen list and make up schools for the students who are not Chosen Ones
for i in not_chosen:
    if len(made_up_schools) >= k - len(chosen_ones):
        break
    if schools[i] not in made_up_schools:
        made_up_schools.add(schools[i])

# Print the number of schools that have been made up
print(len(made_up_schools))
