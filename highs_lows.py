import csv
from datetime import datetime
from matplotlib import pyplot as plt


# Get dates, high, and low temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # next line (headings) is stored in header_row variable. next line after BOF.

    '''
    for index, column_header in enumerate(header_row): # We use enumerate() on the list to get the index of each item, as well as the value.
        print(index, column_header)

    # Now that the indexes are known - using the previous code - then we can extract values using indexes.
    '''
    dates = []
    highs = []
    lows = []

    for row in reader:
        '''
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
        '''
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()   #  draws the date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()


