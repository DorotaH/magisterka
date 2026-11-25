# Read the number of games and the game results from the input
n = int(input())
game_results = input()

# Count the number of games won by Anton and Danik
anton_wins = game_results.count('A')
danik_wins = n - anton_wins

# Determine the winner or the status
if danik_wins < anton_wins:
	print("Anton")
elif danik_wins > anton_wins:
	print("Danik")
else:
	print("Friendship")
