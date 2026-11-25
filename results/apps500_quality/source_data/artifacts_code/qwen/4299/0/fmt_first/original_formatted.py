N = int(input())
ones_place = N % 10
if (
    ones_place == 2
    or ones_place == 4
    or ones_place == 5
    or ones_place == 7
    or ones_place == 9
):
    print("hon")
elif ones_place == 0 or ones_place == 1 or ones_place == 6 or ones_place == 8:
    print("pon")
elif ones_place == 3:
    print("bon")
