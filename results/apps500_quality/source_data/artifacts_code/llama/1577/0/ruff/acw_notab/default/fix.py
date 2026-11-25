n = int(input())
s = input()
anton_wins = s.count('A')
danik_wins = n - anton_wins

if danik_wins < anton_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
