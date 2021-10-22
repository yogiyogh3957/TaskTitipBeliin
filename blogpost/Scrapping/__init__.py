from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-us"
}

class GetImage():

   def __init__(self):
       self.data_list = []


   def getAmazon(self, url):
       response = requests.get(url=url, headers=headers)
       amazon_web_text = response.text
       soup = BeautifulSoup(amazon_web_text, "lxml")

       data_price = soup.find("span", id="price_inside_buybox")
       price = float(data_price.getText().split("$")[1])
       # print(price)

       data_image = soup.find("img", id="landingImage")
       image = data_image['src']
       # print(image)

       data_title = soup.find('h1', id='title')
       title_product = data_title.getText().strip()
       # print(title_product)

       self.data_list.append(price)
       self.data_list.append(image)
       self.data_list.append(title_product)


   def getEbay(self, url):
       pass










