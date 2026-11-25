s = input()
if not any(s[i] == s[i+1] for i in range(len(s)-1)):
    print('Good')
else:
    print('Bad')