#Import all the required libraries
from bs4 import BeautifulSoup
import requests
import time

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
  #Get the URL
  url="https://www.google.com/search?q="+coin+"+price"

  #Make a request to the website
  HTML=requests.get(url)

  #Parse the HTML
  soup=BeautifulSoup(HTML.text,'html.parser')

  #Find the current price
  text=soup.find("div",attrs={'BNeawe iBp4i AP7Wnd'}).find("div",attrs={'BNeawe iBp4i AP7Wnd'}).text

  return text

#Create a main function to consistently show the priceof the cryptocurrency
def main():
  last_price=-1
  #Create an infinite loop to continously show the price

  #Choose the cryptocurrency that you want
  crypto=input("Enter the currency : \n 1.bitcoin \n 2.etherium \n 3.litecoin \n ")


  while True:
    #Get the price of cryptocurrency
    price=get_crypto_price(crypto)

    #Check if the price changed
    if price!=last_price:
      print(crypto+' price:',price)
      #Update the last price
      last_price=price
      #Suspend execution for 3 seconds
      time.sleep(3)

#Calling the main fuction
main()