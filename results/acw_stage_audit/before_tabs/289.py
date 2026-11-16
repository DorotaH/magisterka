def odd_Days(N): 
    hund1 = N // 100
    hund4 = N // 400
    leap = N >> 2
    ordd = N - leap
    if (hund1): 
        ordd += hund1 
        leap -= hund1
    if (hund4): 
        ordd -= hund4 
        leap += hund4
    days = ordd + 2 * leap
    return days % 7
