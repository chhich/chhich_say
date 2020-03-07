import csv
import lxml
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/'
               'Comparison_of_text_editors')
bs = BeautifulSoup(html.'lxml')
table = bs.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

csvfile = open('c:\\users\\MI\\editorscsv','wt+')
writer = csv.writer(csvfile)
try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvfile.close()