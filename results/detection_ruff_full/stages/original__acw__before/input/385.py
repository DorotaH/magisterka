def get_perrin(n):
  if (n == 0):
    return 3
  if (n == 1):
    return 0
  return 2 if (n == 2) else get_perrin(n - 2) + get_perrin(n - 3)