import requests
r=requests.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas+shoes&rh=i%3Aaps%2Ck%3Aadidas+shoes")
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
results=soup.find_all('a' , attrs={'class':'a-link-normal a-text-normal'})
for divdata in soup.find_all('img',attrs={'class':'s-access-image cfMarker','width':'218'}):
    print(divdata['src'])





