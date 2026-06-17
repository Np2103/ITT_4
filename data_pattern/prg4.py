from datetime import datetime

def check_dates(date1, date2):
    d1 = datetime.strptime(date1, "%b %d %Y")
    d2 = datetime.strptime(date2, "%b %d %Y")

    if d1 > d2:
        d1, d2 = d2, d1

    if d2.day == d1.day and ((d2.year - d1.year) * 12 + (d2.month - d1.month)) == 1:
        return "Exactly 1 month apart"

    if (d2 - d1).days < 31:
        return "Less than 1 month apart"

    return "More than 1 month apart"


date1 = input("Enter first date: ")
date2 = input("Enter second date: ")
print(check_dates(date1, date2))
