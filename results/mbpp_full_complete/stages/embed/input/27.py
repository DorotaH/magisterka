import re  
def remove(list): 
    pattern = '[0-9]'
    return [re.sub(pattern, '', i) for i in list]