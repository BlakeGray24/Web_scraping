#
'''
Find a 'scrappable' cryptocurrencies website 
where you can scrape the top 5 cryptocurrencies 
and display as a formatted output one currency at a time. 
The output should display the name of the currency, 
the symbol (if applicable), the current price 
and % change in the last 24 hrs
and corresponding price (based on % change)

Furthermore, for Bitcoin and Ethereum, 
the program should alert you via text 
if the value falls below $40,000 for BTC and $3,000 for ETH.

Submit your GitHub URL which should contain all 
the files worked in class as well as the above.

'''

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://coinmarketcap.com/coins/'
#url = 'https://crypto.com/price'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read().decode(encoding="iso-8859-1")
soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll('tr')

#title = soup.title

#print(title.text)

for row in table_rows[1:6]:
    

    td = row.findAll('td')
    #icon = row.findAll('src')

    #a = row.findAll('a')
    #print(td)
    #img = td[1]
    name = td[2].text
    price = float(td[3].text.replace("$","").replace(",",""))
    change_24hr = float(td[5].text.replace("%",""))
    corr_price = round((price*(change_24hr/100))+price,2)
    
    print("-----------------------------")
    print(f"Name & Icon: {name}")
    #print(f"Icon: {img}")
    print(f"Price: ${price}")
    print(f"24hr % change: {change_24hr}%")
    print(f"Corresponding price (based on % change): ${corr_price}")
    print("-----------------------------")
    input()


import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+18304944580"
myCellphone = '+18325359648'


table_Data = soup.findAll('td')

for row in table_Data[1:2]:

    Check_price_bit = float(table_Data[3].text.replace("$","").replace(",",""))
    Check_price_eth = float(table_Data[15].text.replace("$","").replace(",",""))


    if Check_price_bit < 40000.00:
        Bit = "Bitcoin price has fallen below $40,000! The current price is: $" + str(Check_price_bit)
        textmsg1 =client.messages.create(to=myCellphone,from_=TwilioNumber,body=Bit)
        print(textmsg1.status)


    if Check_price_eth < 3000.00:
    
        Eth = "Ethereum price has fallen below $3000! The current price is: $" + str(Check_price_eth)
        textmsg2 =client.messages.create(to=myCellphone,from_=TwilioNumber,body=Eth)
        print(textmsg2.status)

    #print(Check_price_bit)
    #print(Check_price_eth)




'''
for row in table_rows[1:2]:

    td = row.findAll('td')

    Check_price_bit = float(td[3].text.replace("$","").replace(",",""))


    if Check_price_bit < 40000.00:
        Bit = "Bitcoin price has fallen below $40,000! The current price is: $" + str(Check_price_bit)
        textmsg1 =client.messages.create(to=myCellphone,from_=TwilioNumber,body=Bit)
        print(textmsg1.status)




    Check_price_eth = float(td[3].text.replace("$","").replace(",",""))

    if Check_price_eth < 3000.00:
    
        Eth = "Ethereum price has fallen below $3000! The current price is: $" + str(Check_price_eth)
        textmsg2 =client.messages.create(to=myCellphone,from_=TwilioNumber,body=Eth)
        print(textmsg2.status)

'''







