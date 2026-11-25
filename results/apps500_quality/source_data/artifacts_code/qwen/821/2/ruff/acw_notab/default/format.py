s, v1, v2, t1, t2 = map(int, input().split())

# Time to receive the text and start typing for each participant
time_first = t1 + v1 * s
time_second = t2 + v2 * s

# Determine the result
if time_second > time_first:
    print("First")
elif time_second < time_first:
    print("Second")
else:
    print("Friendship")
