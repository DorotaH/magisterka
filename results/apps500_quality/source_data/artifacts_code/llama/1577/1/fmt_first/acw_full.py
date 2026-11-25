n = int(input())
games = input()

anton_wins = games.count("A")
danik_wins = n - anton_wins

if danik_wins < anton_wins:
	print("Anton")
elif danik_wins > anton_wins:
	print("Danik")
else:
	print("Friendship")
