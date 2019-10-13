from bs4 import BeautifulSoup
import requests
import csv
URL = "https://satvikpadhiyar.wordpress.com"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
time = soup.select('time')[0].get_text()
title = soup.select('.entry-title')[0].get_text().replace
filename = 'inspirational_quotes.csv'
with open(filename, 'w') as f:
    w = csv.writer(f)
    w.writerow(["title", "time"])
    w.writerow(["title", "time"])
    w.writerow(["title", "time"])
