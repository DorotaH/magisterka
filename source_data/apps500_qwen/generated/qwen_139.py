A, B, C = map(int, input().split())
remaining_in_Bottle2 = C - (A - B)
print(max(0, remaining_in_Bottle2))
