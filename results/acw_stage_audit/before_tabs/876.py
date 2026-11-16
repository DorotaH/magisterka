def lcm(x, y):
   z = max(x, y)
   while (True):
       if ((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1
   return lcm
