import csv
import matplotlib.pyplot as plt
from datetime import datetime

#seleciona os arquivos com os dados e o seu formato
dv_file = 'csv/death_valley_2021_simple.csv'
st_file = 'csv/sitka_weather_2021_simple.csv'

#abre os arquivos em modo leitura e parseia

try: 
    with open(dv_file) as f:
    #recura os dados e o header
        reader = csv.reader(f)
        header = next(reader)
            
        dv_dates, dv_highs = [], []
        for row in reader:
            try:
                high = int(row[3])
                current_data = datetime.strptime(row[2], "%Y-%m-%d")
            except:
                print(f'No such data at {len(dv_highs)}')
            else:
                dv_highs.append(high)
                dv_dates.append(current_data)

except FileNotFoundError: 
    print('File not found.')

print(len(dv_dates), len(dv_highs))


try: 
    with open(st_file) as f:
    #recura os dados e o header
        reader = csv.reader(f)
        header = next(reader)
            
        for indice, value in enumerate(header):
            print(indice, value)
        st_dates, st_highs = [], []
        for row in reader:
            try:
                high = int(row[4])
                current_data = datetime.strptime(row[2], "%Y-%m-%d")
            except:
                print(f'No such data at {len(st_highs)}')
            else:
                st_highs.append(high)
                st_dates.append(current_data)

except FileNotFoundError: 
    print('File not found.')



plt.style.use('_mpl-gallery')

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dv_dates, dv_highs, c='red', alpha=0.5)
plt.plot(st_dates, st_highs, c='blue', alpha=0.5)
plt.fill_between(dv_dates, dv_highs, st_highs, facecolor='grey', alpha=0.1)

plt.title('Compare DV and St')
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature', fontsize=16)

fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tight_layout()

plt.show()
