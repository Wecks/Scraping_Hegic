import json
import datetime
import requests
import openpyxl as xl
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# defining key/request url to Binance API
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

#HEGIC LINKS : Staddle strategy 15 days
url_btc_15 = "https://www.hegic.co/app#/arbitrum/trade/new?position=0&sentiment=high&strategyName=high-straddle&strikeName=straddle&period=15&asset=BTC"
url_eth_15 = "https://www.hegic.co/app#/arbitrum/trade/new?position=0&sentiment=high&strategyName=high-straddle&strikeName=straddle&period=15&asset=ETH"
#HEGIC LINKS : Staddle strategy 30 days
url_btc_30 = "https://www.hegic.co/app#/arbitrum/trade/new?position=0&sentiment=high&strategyName=high-straddle&strikeName=straddle&period=30&asset=BTC"
url_eth_30 = "https://www.hegic.co/app#/arbitrum/trade/new?position=0&sentiment=high&strategyName=high-straddle&strikeName=straddle&period=30&asset=ETH"

class element_doesnt_have_text(object):
  """An expectation for checking that an element has a particular text.

  locator - used to find the element
  returns the WebElement once it has the particular text
  """
  def __init__(self, locator, text):
    self.locator = locator
    self.text = text

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.text not in element.text:
        return element
    else:
        return False

# Wait until an element with id='myNewInput' has class 'myCSSClass'
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# options.binary_location = "../usr/bin/google-chrome"
# chrome_driver_binary = "./chromedriver"

driver = webdriver.Chrome()
driver.get(url_btc_15)

elem_premium_btc = driver.find_element(By.CLASS_NAME, "trade-new-selects-buttons-box-info-elem")
wait = WebDriverWait(elem_premium_btc, 10)

# Waiting until the price of the premium shows up
premium_btc = wait.until(element_doesnt_have_text((By.TAG_NAME, "span"), "..."))

# requesting data from url : Binance API
data = requests.get(key)  
data = data.json()
premium = premium_btc.text
data['price'] = data['price'].split('.')[0]

print(premium + " " + data['price'])

driver.close()
# Putting everything in an excel
wb = xl.load_workbook(filename='Premium.xlsx')
print("in excel")
sheet = wb.active

if not sheet["A1"].value:
   sheet["A1"].value = "Date UTC"
if not sheet["B1"].value:
   sheet["B1"].value = "Pair"
if not sheet["C1"].value:
   sheet["C1"].value = "Durée"
if not sheet["D1"].value:
   sheet["D1"].value = "Prix"
if not sheet["E1"].value:
   sheet["E1"].value = "Premium"

def table_index(colum):
   for i in range(200,1000):
      if not sheet[colum+str(i)].value:
         return str(i)

index = table_index("A")
print("After index :"+index)

sheet["A"+index].value = datetime.datetime.today()
sheet["B"+index].value = "BTC/USD"
sheet["C"+index].value = 15
sheet["D"+index].value = data['price']
sheet["E"+index].value = premium.replace(" ","")
print(premium.replace(" ",""))
wb.save('Premium.xlsx')
wb.close()
