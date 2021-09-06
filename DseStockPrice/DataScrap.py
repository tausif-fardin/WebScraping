import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://www.dse.com.bd/day_end_archive.php?startDate=2019-09-05&endDate=2021-09-05&inst=All%20Instrument&archive=data#'

r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {
                  "class": "table table-bordered background-white shares-table fixedHeader"})
rows = table.find_all('tr')
data = []

file = open('dsedata.csv', 'w')
writer = csv.writer(file)

# write header rows
# writer.writerow(data)

for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    writer.writerow(data[-1])

result = pd.DataFrame(data, columns=['#', 'DATE', 'TRADING CODE', 'LTP*',
                      'HIGH', 'LOW', 'OPENP*', 'CLOSEP*', 'YCP', 'TRADE', 'VALUE (mn)', 'VOLUME'])

print(result)

file.close()
