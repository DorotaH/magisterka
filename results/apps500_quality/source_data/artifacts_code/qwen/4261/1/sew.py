A, B, C = map(int, input().split())
remaining_in_bottle_2 = C - (A - B)
print(max(0, remaining_in_bottle_2))