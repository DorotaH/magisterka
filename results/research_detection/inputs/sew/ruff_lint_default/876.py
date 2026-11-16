def lcm(x, y):
   z = max(y, x)
   while(True):
       if((0 == z % x) and  (0 == z % y)):
           lcm=z
           break
       z += 1
   return lcm
