def decimal_to_Octal(deciNum):
    octalNum = 0
    countval = 1;
    dNo=deciNum;
    while  (0!= deciNum):
        remainder= deciNum % 8;
        octalNum= octalNum+ remainder*countval;
        countval= countval*10;
        deciNum = deciNum // 8; 
    return (octalNum)