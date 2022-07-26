from datetime import date

dob = date(1998, 7, 13)

print((date.today() - dob).days // 365)