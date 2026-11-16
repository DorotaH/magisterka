def dog_age(h_age):
	if h_age < 0:
		exit()
	elif 2 >= h_age:
		d_age = h_age * 10.5
	else:
		d_age = 21 + (h_age - 2) * 4
	return d_age
