n, s = int(input()), input()
anton_wins, danik_wins = s.count('A'), s.count('D')

if  danik_wins < anton_wins:
    print("Anton")
elif  danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
