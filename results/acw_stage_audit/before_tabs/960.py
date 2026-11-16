def get_noOfways(n):
    if (n == 0):
        return 0;
    return 1 if (n == 1) else get_noOfways(n - 2) + get_noOfways(n - 1)
