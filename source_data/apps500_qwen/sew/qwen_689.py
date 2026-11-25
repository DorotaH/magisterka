from  collections import  Counter
import sys

def can_form_good_string(s):
    count=Counter(s)
    odd_count=sum(1 for v in count.values() if 0 != v % 2)
    return odd_count <= 1

def rearrange_to_good_string(s):
    if not can_form_good_string(s):
        return -1
    count=Counter(s)
    odd_chars, even_chars = [char for char, freq in count.items() if freq % 2 != 0], [char for char, freq in count.items() if freq % 2 == 0]
    odd_chars.sort()
    even_chars.sort()
    result=odd_chars+even_chars
    return ''.join(result)

def main():
    input=sys.stdin.read
    data=input().split()
    t, results = int(data[0]), []
    for i in range(t):
        s = data[i + 1]
        result = rearrange_to_good_string(s)
        results.append(result)
    for result in results:
        print(result)

if  __name__=="__main__":
    main()
