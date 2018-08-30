from modules.date import date

def calcDateDiff(inpDate1, inpDate2):
    dayCount = 0
    
    # Find the earliar date
    if inpDate1.isBefore(inpDate2):
        start = inpDate1
        end = inpDate2
    else:
        start = inpDate2
        end = inpDate1
        
    # Balancing the days
    while start.getDate() != end.getDate():
        start.dateIncrement()
        dayCount += 1

    while start.getMonth() != end.getMonth():
        dayCount += start.getDaysInMonth()
        start.monthIncrement()

    while start.getYear() != end.getYear():
        if start.isBefore(date(29, 2, start.getYear())):
            if start.isLeapYear():
                dayCount += 366
            else:
                dayCount += 365
        else:
            if date(1,1,start.getYear()+1).isLeapYear():
                dayCount += 366
            else:
                dayCount += 365 
        start.yearIncrement()

    return dayCount-1

