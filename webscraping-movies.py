
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import openpyxl as xl
#from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

table_rows = soup.findAll("tr")

print(title.text)
##
for row in table_rows[1:6]:
    td = row.findAll("td")


    rank = td[0].text
    release = td[1].text
    theaters = int(td[6].text.replace(",",""))
    total_gross = int(td[7].text.replace("$","").replace(",",""))
    distributor = td[9].text

    avg_profit = round((total_gross/theaters),2)

    print("-------------------------------------------")
    print(f"Movie Rank: {rank}")
    print(f"Movie Name: {release}")
    print(f"Total Gross Profit: ${total_gross}")
    print(f"Theaters: {theaters}")
    print(f"Average revenue per theater: ${avg_profit}")
    print(f"Distributor: {distributor}")
    print("-------------------------------------------")
'''
movie_rows = soup.findAll('tr')

print(movie_rows)

for x in range(1,6)
td = movie_rows[x].findAll('td')
print(td[0])
'''
