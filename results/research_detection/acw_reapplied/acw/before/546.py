def last_occurence_char(string, char):


flag = -1
for i in range(len(string)):
	if (string[i] == char):
		flag = i
return None if (flag == -1) else flag + 1
