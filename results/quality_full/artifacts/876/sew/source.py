def lcm(x, y):
   z = x if x > y else y
   while(True):
       if((0 == z % x) and  (0 == z % y)):
           lcm=z
           break
       z += 1
   return lcm
