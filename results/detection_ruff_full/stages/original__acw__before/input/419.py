def round_and_sum(list1):
  lenght=len(list1)
  return sum(list(map(round,list1))* lenght)