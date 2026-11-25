s = input()
t = input()
position = 1
for i in range(len(t)):
    if  t[i] == "R" and  s[position - 1] == "R":
        position = position + 1
    elif  t[i] == "G" and  s[position - 1] == "G" or t[i] == "B" and  s[position - 1] == "B":
        position += 1
print(position)