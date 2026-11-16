def cal_electbill(units):
 if (units < 50):
    amount = 2.60 * units
    surcharge = 25
 elif (units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
 elif (units <= 200):
    amount = 162.50 + 130 + ((units - 100) * 5.26)
    surcharge = 45
 else:
    amount = 162.50 + 130 + 526 + (8.45 * (units - 200))
    surcharge = 75
 return amount + surcharge
