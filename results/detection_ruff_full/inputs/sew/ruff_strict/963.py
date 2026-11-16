def discriminant_value(x, y, z):
    discriminant = (y**2) - 4 * x * z
    if discriminant > 0:
        return ("Two solutions", discriminant)
    if discriminant == 0:
        return ("one solution", discriminant)
    if discriminant < 0:
        return ("no real solution", discriminant)
