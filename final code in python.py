import csv
import requests
import urllib.request
from numpy import genfromtxt, savetxt
# r=requests.get("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas+shoes&rh=i%3Aaps%2Ck%3Aadidas+shoes")
import http.client
conn = http.client.HTTPSConnection("www.amazon.in")
conn.request("GET", "/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas%20shoes&rh=i%3Aaps%2Ck%3Aadidas%20shoes")
res = conn.getresponse()
data = res.read()
# print data
# r = data.decode("utf-8")
from bs4 import BeautifulSoup
soup=BeautifulSoup(data)
with open("final.csv", "w") as output:
        output.write("Title ")
# #finding the Title of each shoes
count = 0
# print str(data)
# print soup.find_all('h2')
for head in soup.find_all('h2'):
    with open("final.csv", "a") as output:
        a=str(head.contents)
        a=a.replace(',',' ')
        print(a)
        print (count)
        count = count+1
        output.write("," + str(head.contents) )
with open("final.csv", "a") as output:
    output.write('\n')
    output.write('Image')
# #finding the pictures
results=soup.find_all('a' , attrs={'class':'a-link-normal a-text-normal'})
for divdata in soup.find_all('img',attrs={'class':'s-access-image cfMarker'}):
    with open("final.csv", "a") as output:
        print(divdata['src'])
        output.write("," + str(divdata['src']))
with open("final.csv", "a") as output:
    output.write('\n')
    output.write('Currency in(Rs.)')
# #finding the price range
for amount in soup.find_all('span', attrs={'class':'a-size-base a-color-price s-price a-text-bold'}):
    ans=str(amount)
    last=ans[95:-7]
    x=last[:5]
    y=last[-5:]
    x=x.replace(',',' ')
    y=y.replace(',',' ')
    print(x," - ",y)
    with open("final.csv", "a") as output:
        output.write(',' + str(x) + " -" + str(y)+',')
    output.close()










# """with open("final.csv", "w") as output:
#     output.write('Name,Picture,Price\n')
#     output.write(str(first_title.contents) + divdata['src'] + str(x) + '-'+ str(y) + '\n')
#     output.close("final.csv")
#    """
