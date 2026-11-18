class NumericEntityUnescaper:
    def __init__(self):
        ...
    def replace(self, string):
        out = list()
        pos = 0
        length = len(string)

        while  pos<length-2:
            if  string[pos] == '&' and  string[1 + pos] == '#':
                start = pos + 2
                is_hex, first_char = False, string[start]

                if first_char in ('x', 'X'):
                    start = start + 1
                    is_hex = True

                if start == length:
                    return  ''.join(out)

                end = start
                while length > end and self.is_hex_char(string[end]):
                    end += 1

                if end < length and string[end] == ';':
                    try:
                        entity_value = int(string[start:end], 16 if  is_hex else 10)
                    except:
                        return ''.join(out)

                    out.append(chr(entity_value))
                    pos = end + 1
                    continue

            out.append(string[pos])
            pos = pos + 1

        return  ''.join(out)
    @staticmethod
    def  is_hex_char(char):
        return  char.isdigit() or  ('a' <= char.lower() <= 'f')