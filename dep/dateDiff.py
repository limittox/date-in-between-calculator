"""
Months have different days
Leap years

Design v1:
    Convert input to list (done)
    Find input which is going to be the start date (done)
    Calculate days difference
        Balance the day first, then count using months

> Calculate the number of leap years between the dates
"""
# start_date = input("Start date: ").split('/')
# end_date = input("End date: ").split('/')

from modules.date import date

inpDate1 = "03/01/1989"
inpDate2 = "03/08/1983"

inpDate1 = [int(s) for s in inpDate1.split('/')]
inpDate2 = [int(s) for s in inpDate2.split('/')]

def calcDaySpan(inpDate1, inpDate2):
    dayCount = 0
    
    # inp1 = date(inpDate1[0], inpDate1[1], inpDate1[2])
    # inp2 = date(inpDate2[0], inpDate2[1], inpDate2[2])

    # Find the earliar date
    for i in range(2,-1,-1):
        if inpDate1[i] == inpDate2: 
            continue
        if inpDate1[i] < inpDate2[i]:
            start = date(inpDate1[0], inpDate1[1], inpDate1[2])
            end = date(inpDate2[0], inpDate2[1], inpDate2[2])
        else: 
            start = date(inpDate2[0], inpDate2[1], inpDate2[2])
            end = date(inpDate1[0], inpDate1[1], inpDate1[2])
            
    # Find the earliar date
    # for i, j in zip(reversed(inpDate1), reversed(inpDate2)):
    #     if i != j:
    #         if min(i, j) == i:
    #             start_date = inpDate1
    #             end_date = inpDate2
    #             break
    #         else:
    #             start_date = inpDate2
    #             end_date = inpDate1
    #             break


    # start = date(start_date[0], start_date[1], start_date[2])
    # end = date(end_date[0], end_date[1], end_date[2])
    
    # Balancing the days
    while start.getDate() != end.getDate():
        start.dateIncrement()
        dayCount += 1
        # print(dayCount)

    while start.getMonth() != end.getMonth():
        # print(start.getMonth(), end=': ')
        start.monthIncrement()
        dayCount += start.getDaysInPrevMonth()
        # print(start.getDaysInPrevMonth())

    while start.getYear() != end.getYear():
        # print(start.getYear(), end=': ')
        # start.yearIncrement()
        if start.isLeapYear():
            dayCount += 366
            # print(366)
        else:
            dayCount += 365
            # print(365)
        start.yearIncrement()
        # print(dayCount)
    # test = date(20,2,1984)
    # print(test.isLeapYear())
    print(dayCount-1)
    print(inpDate1)
    print(inpDate2)

calcDaySpan(inpDate1, inpDate2)