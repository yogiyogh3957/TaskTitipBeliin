from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-us"
}

proxies = { 'http': "http://52.185.165.115:8000",
            'https': "https://197.255.52.214:8081",}

class GetImage():

   def __init__(self):
       self.notfound = ["not found", "https://images.bizlaw.id/gbr_artikel/images-2_294.webp", "Not Found title"]
       self.data_list = []

   def getAmazon(self, url):
                                                        #DELETE PROXIES IF RUNNING LOCALY
       response = requests.get(url=url, headers=headers, proxies=proxies, timeout=None)
       amazon_web_text = response.text
       soup = BeautifulSoup(amazon_web_text, "html.parser")


       try:
            data_price = soup.find("span", id="price_inside_buybox")
            price = float(data_price.getText().split("$")[1])
       except AttributeError :
           data_price = soup.find("span", id="a-color-price a-text-bold")
           price = data_price
       except TypeError :
           price = None

       try:
            data_image = soup.find("img", id="landingImage")
            image = data_image['src']
       except TypeError:
            data_image = soup.find("img", id="gc-standard-design-image")
            try:
                image = data_image['src']
            except TypeError :
                image = None
       # print(image)


       try:
            data_title = soup.find('h1', id='title')
            title_product = data_title.getText().strip()
       except AttributeError :
           data_title = soup.find('span', id='gc-asin-title')
           try:
                title_product = data_title.getText().strip()
           except AttributeError :
                title_product = None
       # print(title_product)

       if price == None and image == None and title_product == None :
            self.data_list = self.notfound
       # print(price)

       else:

           self.data_list.append(price)
           self.data_list.append(image)
           self.data_list.append(title_product)

###########################################################################################################

   def getEbay(self, url):
       response = requests.get(url=url, headers=headers)
       ebay_web_text = response.text
       soup = BeautifulSoup(ebay_web_text, "html.parser")

       try:
           data_price = soup.find("span", id='prcIsum')
           price = data_price.getText()
       except AttributeError :
           try:
               data_price = soup.find("span", id='prcIsum_bidPrice')
               price = data_price.getText()
           except AttributeError :
               try:
                   data_price = soup.find("span", id='mm-saleDscPrc')
                   price = data_price.getText()
               except AttributeError :
                   price = None

       try:
           data_image = soup.find("img", id="icImg")
           image = data_image['src']
       except AttributeError :
           image = None
       # print(image)


       try:
           data_title = soup.find('h1', id='itemTitle').getText().split(" ")
           title_product = ""
           for x in range(4, len(data_title)):
               title_product+= data_title[x] + " "
       except AttributeError :

           title_product = None
       # print(title_product)

       if price == None and image == None and title_product == None :
            self.data_list = self.notfound
       # print(price)

       else:

           self.data_list.append(price)
           self.data_list.append(image)
           self.data_list.append(title_product)










