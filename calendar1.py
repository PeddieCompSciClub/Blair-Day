from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC  # timezone
from datetime import date
from datetime import datetime
import datetime
from dateutil import relativedelta

# Returns the current local date
todayDate = date.today()
todayMonth = str(todayDate)
todayMonth = todayMonth[5:7]
todayDay = str(todayDate)
todayDay = todayDay[8:]
nextMonth = datetime.date.today() + relativedelta.relativedelta(months=1)
nextMonth2 = str(nextMonth)
nextMonth2 = nextMonth2[5:7]
nextDay = str(nextMonth)
nextDay = nextDay[8:]
actualDay = date.today().day
actualDay = str(actualDay)
todayMonth2 = todayDate.strftime("%B")
nextMonth3 = nextMonth.strftime("%B")
file1 = open("calendar1.txt", "w")


def findCalendar(textFile):
    g = open(textFile, "rb")
    gcal = Calendar.from_ical(g.read())
    for component in gcal.walk():
        if component.name == "VEVENT":
            startTime = component.get("DTSTART").to_ical()
            startTimeString = startTime.decode("utf-8")
            startTimeString1 = startTimeString[4:6]
            startTimeString2 = startTimeString[6:8]
            if (
                startTimeString1 == todayMonth
                and startTimeString2 >= nextDay
                or startTimeString1 == nextMonth2
                and startTimeString2 <= actualDay
            ):
                menu = component.get("summary")
                menu2 = component.get("location")

                if menu != None and menu2 != None:
                    file1.write(menu)

                    file1.write("\n")

                    file1.write(menu2)
                    file1.write("\n")
                elif menu != None:
                    file1.write(menu + " - ")
                    if startTimeString1 == todayMonth:
                        file1.write("\t" + todayMonth2)
                    elif startTimeString1 == nextMonth2:
                        file1.write("\t" + nextMonth3)
                    file1.write("\t" + startTimeString2)
                    file1.write("\n")
            else:
                menu = ""
                file1.write(menu)

    g.close()


findCalendar("calendar1.ics")
file1.close()

#debugging:
print(__file__)