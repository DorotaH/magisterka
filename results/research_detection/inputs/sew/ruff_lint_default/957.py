import math


def  get_First_Set_Bit_Pos(n):
     return  1+math.log2(n&-n)
