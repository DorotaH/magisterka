def first_even(nums):
    return next((el for el in nums if el%2==0),-1)