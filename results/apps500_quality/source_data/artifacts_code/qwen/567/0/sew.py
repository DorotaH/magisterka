def  min_time_to_pick_prizes(n, a):
    # Calculate the minimum time to pick all prizes
    # The strategy is to have one person start from position 1 and the other from position 10^6
    # They will meet in the middle, and then one will continue to the left and the other to the right
    # The time taken will be the maximum of the time each person takes to reach the middle and then to their respective side
    mid = (10**6) // 2
    time_to_mid, time_to_other_side = max(abs(a[0] - 1), abs(a[-1] - mid)), max(abs(a[0] - mid), abs(a[-1] - 10**6))
    return  time_to_other_side + time_to_mid

# Read input
import  sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))

# Output the result
print(min_time_to_pick_prizes(n, a))