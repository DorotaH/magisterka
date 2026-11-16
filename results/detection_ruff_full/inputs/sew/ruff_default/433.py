def check_greater(arr, number):
    arr.sort()
    if not number > arr[-1]:
        return "No, entered number is less than those in the array"
    else:
        return "Yes, the entered number is greater than those in the array"
