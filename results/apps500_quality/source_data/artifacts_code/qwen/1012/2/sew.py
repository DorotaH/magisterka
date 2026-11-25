def can_form_good_string(s):
    from  collections import  Counter
    count = Counter(s)
    odd_count = sum(1 for  v in  count.values() if  0 != v % 2)
    if not odd_count > 1:
        return s
    else:
        return -1


def rearrange_to_good_string(s):
    from  collections import  Counter
    count = Counter(s)
    odd_chars, even_chars = [char for char, freq in count.items() if freq % 2 != 0], [char for char, freq in count.items() if freq % 2 == 0]
    
    if len(odd_chars) > 1:
        return  -1
    
    if not len(odd_chars) == 1:
        result = [even_char] * (len(even_chars) // 2)
    else:
        odd_char = odd_chars[0]
        even_char = even_chars[0]
        result = [even_char] * (len(even_chars) // 2) + [odd_char] + [even_char] * (len(even_chars) // 2)
    
    return ''.join(result)


def main():
    import  sys
    input = sys.stdin.read
    data = input().split()
    
    t, queries = int(data[0]), data[1:]
    
    results = []
    for  query in  queries:
        if len(query) == 1:
            results.append(-1)
        else:
            result = rearrange_to_good_string(query)
            if result == -1:
                results.append(result)
            else:
                results.append(result)
    
    for  result in  results:
        print(result)

if  __name__=="__main__":
    main()
