import csv
import matplotlib.pyplot as plt
from datetime import datetime
filename = './csv/death_valley_2021_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:

        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        try:
            high = int(row[4])
            low  = int(row[5])
        except ValueError:
            print(f'Missing value at {len(highs)}.')
        else:
            dates.append(current_date)
            highs.append(high)        
            lows.append(low)


    plt.style.use('_mpl-gallery')

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title("Daily high and low temperatures - 2021\nDeath Valley, CA", fontsize=20)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    
    fig.autofmt_xdate()

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.tight_layout()

    plt.show()

