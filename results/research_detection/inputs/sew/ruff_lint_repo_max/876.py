def lcm(x, y):
   z = max(y, x)
   while(True):
       if((z % x == 0) and  (z % y == 0)):
           lcm=z
           break
       z += 1
   return lcm
