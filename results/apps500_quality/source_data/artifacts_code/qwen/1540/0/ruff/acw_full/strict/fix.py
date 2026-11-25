

def process_chat_log(n, m, k, a, events):
	# Initialize the count of notifications for each employee
	notifications = [0] * n

	# Process each event in the log
	for x, y in events:
		# Increment the notification count for each employee in chat y except the sender
		for i in range(n):
			if a[i][y - 1] == 1 and i != x - 1:
				notifications[i] += 1

	return notifications


# Read input
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
events = [tuple(map(int, input().split())) for _ in range(k)]

# Process the chat log and get the notifications
result = process_chat_log(n, m, k, a, events)

# Print the result
print(" ".join(map(str, result)))
