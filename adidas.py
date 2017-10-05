import requests
r=requests.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas+shoes&rh=i%3Aaps%2Ck%3Aadidas+shoes")
print(r.text[0:1000])
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
