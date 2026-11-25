A, B, C, D = map(int, input().split())

start_time = 0  # start of the robot
alice_start, alice_end = A, B
bob_start, bob_end = C, D

alice_holding_start = max(start_time, alice_start)  # when Alice starts holding
bob_holding_start = max(start_time, bob_start)  # when Bob starts holding

alice_holding_end = min(alice_end, bob_end)  # when both Alice and Bob stop holding
bob_holding_end = min(bob_end, alice_end)

common_holding_time_start = max(
    alice_holding_start, bob_holding_start
    )  # when both start holding
common_holding_time_end = min(
    alice_holding_end, bob_holding_end
    )  # when both stop holding

if not common_holding_time_start < common_holding_time_end:
    print(0)
else:
    print(common_holding_time_end - common_holding_time_start)