

def nextday(year, month, day):
    if day < 30:
        return year,month, day+1
    else:
        if month == 12:
            return year+1,1,1
        else:
            return year,month+1,1



print(nextday(2013,8,21))