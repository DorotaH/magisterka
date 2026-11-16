from collections import Counter
from itertools import chain
def freq_element(nums):
  return Counter(chain.from_iterable(nums))