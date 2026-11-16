def discriminant_value(x,y,z):
    discriminant = (y**2) - 4*x*z
    if discriminant>0:
        return ("Two solutions",discriminant)
    elif 0 == discriminant:
        return  ("one solution",discriminant)
    elif discriminant < 0:
        return  ("no real solution",discriminant)