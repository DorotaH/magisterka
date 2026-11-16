def count_char(string,char):
 count=0
 for i in range(len(string)):
    if(char == string[i]):
        count += 1
 return count
