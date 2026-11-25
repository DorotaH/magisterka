def min_schools_to_make_up(n, m, k, powers, schools, chosen_ones):
	# Create a list of tuples (power, school, student_id) and sort it by power in descending order
	students = sorted([(powers[i], schools[i], i + 1) for i in range(n)], reverse=True)

	# Initialize a set to keep track of schools that will be made up
	made_up_schools = set()

	# Initialize a set to keep track of students who are already chosen
	chosen_students = set()

	# Iterate over the sorted students and try to make up schools for the chosen ones
	for power, school, student_id in students:
		if student_id in chosen_students:
			continue
		if student_id not in chosen_ones:
			# If the student is not a chosen one, check if the school is already made up
			if school in made_up_schools:
				continue
			# If the school is not made up, make it up and add the student to the chosen ones
			made_up_schools.add(school)
		chosen_students.add(student_id)
		# If we have enough chosen ones, break the loop
		if len(chosen_students) == k:
			break

	# Return the number of schools made up
	return len(made_up_schools)


# Read input from standard input
n, m, k = map(int, input().split())
powers = list(map(int, input().split()))
schools = list(map(int, input().split()))
chosen_ones = list(map(int, input().split()))

# Call the function and print the result
print(min_schools_to_make_up(n, m, k, powers, schools, chosen_ones))
