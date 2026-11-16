def month_season(month, days):
	if month in ("January", "February", "March"):
		season = "winter"
	elif month in ("April", "May", "June"):
		season = "spring"
	elif month in ("July", "August", "September"):
		season = "summer"
	else:
		season = "autumn"
	if (month == "March") and (days > 19):
		season = "spring"
	elif (month == "June") and (20 < days):
		season = "summer"
	elif (
		((month == "September") and (days > 21))
		or ((month == "October") and (days > 21))
		or ((month == "November") and (days > 21))
	):
		season = "autumn"
	elif (month == "December") and (20 < days):
		season = "winter"
	return season
