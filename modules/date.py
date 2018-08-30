days_in_months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

class date(object):
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year
    
    def getDate(self):
        return self.date

    def setDate(self, date):
        if date > 31 or date < 1:
            print("Error: Date val out of bounds")
            return
        self.date = date
        
    def getMonth(self):
        return self.month

    def setMonth(self, month):
        if month > 12 or month < 1:
            print("Error: Month val out of bounds")
            return
        self.month = month

    def getYear(self):
        return self.year

    # def setYear(year):

    def getDaysInMonth(self):
        if self.isLeapYear() and self.getMonth() == 2:
            return 29
        return days_in_months.get(self.month)
    
    def getDaysInPrevMonth(self):
        if self.isLeapYear() and self.getMonth() == 3:
            return 29
        if self.getMonth() == 1: return 31
        return days_in_months.get(self.getMonth()-1)

    def dateIncrement(self):
        if self.getDate() == self.getDaysInMonth():
            self.setDate(1)
            self.monthIncrement()
        else:
            self.date += 1

    def monthIncrement(self):
        if self.getMonth() == 12:
            self.setMonth(1)
            self.yearIncrement()
        else:
            self.month += 1
    
    def yearIncrement(self):
        self.year += 1

    def isLeapYear(self):
        if self.getYear() % 4 == 0:
            if self.getYear() % 100 == 0:
                if self.getYear() % 400 == 0:
                    return True
                else:
                    return False
            return True
        return False

    def toString(self):
        print(f'{self.getDate()}/{self.getMonth()}/{self.getYear()}')


    def isBefore(self, date):
        if self.getYear() < date.getYear():
            return True
        elif self.getYear() > date.getYear():
            return False

        if self.getMonth() < date.getMonth():
            return True
        elif self.getMonth() > date.getMonth():
            return False

        if self.getDate() < date.getDate():
            return True
        elif self.getDate() < date.getDate():
            return False

        return False

    def isAfter(self, date):
        if self.isBefore(date) is True:
            return False
        return True
