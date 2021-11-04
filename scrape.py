import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.nl/dp/B08H93ZRLL/ref=cm_sw_r_awdo_navT_g_MAXKAGZ81DFG08VPJNXZ' #NL Listing


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle")
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 650):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():