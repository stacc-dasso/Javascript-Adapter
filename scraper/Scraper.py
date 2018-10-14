import urllib.request
from bs4 import BeautifulSoup
import csv

# Test link
quote_page = 'https://www.richelieu.com/us/en/category/screws-and-fasteners/anchors/1057786'
page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')


# writing into CSV
def writeToCSV(argument):
    with open("index.csv", "a") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(argument)


# Takes all href links from DOM
for a in soup.find_all('a', href=True):
    writeToCSV([a['href']])
