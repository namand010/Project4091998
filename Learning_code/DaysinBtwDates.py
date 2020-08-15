def isleapyear(year):
    if year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False

def DaysInmonth(year,month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isleapyear(year):
                return 29
            else:
                return 28
    return 30

def nextDay(year,month,day):
    if day < DaysInmonth(year,month):
        return year,month,day + 1
    else:
        if month == 12:
            return year+1,1,1
        else:
            return year, month+1, 1

def DatesBetweenBig(year1,month1,day1,year2,month2,day2):
    if year2 > year1:
        return True
    if year1 == year2:
        if month2 > month1:
            return True
        if month1 == month2:
            return day2 > day1
    return False



def DaysBetweenDates(year1,month1,day1,year2,month2,day2):
    days = 0
    while DatesBetweenBig(year1,month1,day1,year2,month2,day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    TestCases = ((2012, 9, 30, 2014, 10, 30), 30),\
                ((2012, 1, 1, 2013, 1, 1),366)
    for args, answer in TestCases:
        result = DaysBetweenDates(*args)
        if result == answer:
            print("The Result is {}".format(result))
        else:
            print(result)


    #assert DaysBetweenDates(2012, 9, 30, 2012, 10, 30) == 30, "Failed"

    #assert DaysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366, "Failed"

    #assert DaysBetweenDates(2012, 9, 1, 2012, 9, 4) == 3, "Failed"


test()