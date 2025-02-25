import datetime
import re

def agesList():
    ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
    limitedAges : int = []
    sortedAges = sorted(ages)
    totalAges = len(ages)
    print(f"There are {totalAges} ages in total")
    for age in ages:
        #print(age+1)
        if age >= 16 and age <= 25:
            limitedAges.append(int(age))
    
    print(f"There are {len(limitedAges)} ages between 16 and 25")    
    print(f"Sorted full ages list = {sortedAges}")    
    print(f"The proportion of ages between 16 and 25 is {(len(limitedAges)/len(ages)*100)}%")
  
    
def timeCalc():
    select = int(input("1- Add 2 times\n2- Find the difference between 2 times\n3- Convert to Hours\n4- Convert to Minutes\n5- Convert Minutes to Time\n6- Convert Hours to Time\n7- Convert Days to Time\n8- Exit\n"))

    match select:
        case 1:
            day1, hour1, min1 = getTime()
            time1 = datetime.timedelta(days=day1, hours=hour1, minutes=min1)
            day2, hour2, min2 = getTime()
            time2 = datetime.timedelta(days=day2, hours=hour2, minutes=min2)
            print(f"Combined Time = {time1+time2}")
        case 2:
            day1, hour1, min1 = getTime()
            time1 = datetime.timedelta(days=day1, hours=hour1, minutes=min1)
            day2, hour2, min2 = getTime()
            time2 = datetime.timedelta(days=day2, hours=hour2, minutes=min2)
            print(f"Time Difference = {time1-time2}")
        case 3:
            day1, hour1, min1 = getTime()
            time1 = datetime.timedelta(days=day1, hours=hour1, minutes=min1)
            print(f"Total Hours: {time1.total_seconds()/3600}")
        case 4:
            day1, hour1, min1 = getTime()
            time1 = datetime.timedelta(days=day1, hours=hour1, minutes=min1)
            print(f"Total Minutes: {time1.total_seconds()/60}")
        case 5:
            min = int(input("Enter Minutes: "))
            days = 0
            hours = 0
            mins = 0
            days = min / 1440     
            leftover_minutes = min % 1440
            hours = leftover_minutes / 60
            mins = min - (days*1440) - (hours*60)
            print(str(days) + " days, " + str(hours) + " hours, " + str(mins) +  " mins. ")
        case 6:
            hours = int(input("Enter Hours: "))
            time = hours * 60 * 60
            day = time // (24 * 3600)
            time = time % (24 * 3600)
            hour = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
        case 7:
            day = int(input("Enter Days: "))
        case 8:
            exit()


def getTime():
    timeinput = input("Enter times in DD:HH:MM\n").split()
    for time in timeinput:
        day, hour, min = [int(i) for i in time.split(":")]
    return day, hour, min


def checkPalindrome():
    word = str(input("Enter String: "))
    cleaned = re.sub(r'[^A-Za-z]', '', word).lower()
    print(cleaned)
    print(cleaned[::-1])
    if cleaned == cleaned[::-1]:
        print("Is A Palindrome")
    else:
        print("NOT A Palindrome")






