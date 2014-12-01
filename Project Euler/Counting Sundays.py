days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
days30 = ['February', 'April', 'June', 'September', 'November']
counter = 0
dayCounter = 0
for year in range(1900, 2000):
    for month in months:
        if month in days30:
            if month == 'February':
                if year % 400 == 0:
                    numDays = 28
                elif year % 100 == 0:
                    numDays = 29
                elif year % 4 == 0:
                    numDays = 28
                else:
                    numDays = 29
            else:
                numDays = 30
        else:
            numDays = 31
        for day in range(1, numDays):
            if year > 1900 and day == 1 and days[dayCounter] == 'Sunday':
                counter += 1
            if dayCounter < 6:
                dayCounter += 1
            else:
                dayCounter = 0
print(counter)
