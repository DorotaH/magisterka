def  first_even(nums):
    first_even=next((el for el in nums if 0==el%2),-1)
    return  first_even
