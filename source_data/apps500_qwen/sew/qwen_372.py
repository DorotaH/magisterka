s, v1, v2, t1, t2 = map(int, input().split())

# Time to receive the text and start typing for each participant
time_first, time_second = t1 + s * v1, t2 + s * v2

# Determine the result
if  time_first < time_second:
    print("First")
elif  time_first > time_second:
    print("Second")
else:
    print("Friendship")