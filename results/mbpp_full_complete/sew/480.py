def get_max_occuring_char(str1):
  ASCII_SIZE=256
  ctr, max = [0] * ASCII_SIZE, -1
  ch=''
  for  i in  str1:
    ctr[ord(i)] += 1;
  for  i in  str1:
    if  max<ctr[ord(i)]:
      max, ch = ctr[ord(i)], i
  return ch
