def check_Type_Of_Triangle(a, b, c):
    sqa = a**2
    sqb = b**2
    sqc = c**2
    if sqa == sqa + sqb or sqb == sqa + sqc or sqc == sqa + sqb:
        return "Right-angled Triangle"
    if sqa > sqb + sqc or sqb > sqa + sqc or sqc > sqa + sqb:
        return "Obtuse-angled Triangle"
    return "Acute-angled Triangle"
