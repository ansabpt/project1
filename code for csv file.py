import csv
import requests
from numpy import genfromtxt, savetxt
import http.client

conn = http.client.HTTPSConnection("www.amazon.in")
conn.request("GET", "/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=adidas%20shoes&rh=i%3Aaps%2Ck%3Aadidas%20shoes")

res = conn.getresponse()
data = res.read()
shoe_dict = {}
from bs4 import BeautifulSoup
import pickle
soup=BeautifulSoup(data,'html.parser')
for litag in soup.find_all("li",id=lambda x: x and x.startswith('result_')):
	s_id =  litag['id']
	title =  litag.find('h2').text
	img_url = litag.find('img')['src']
	amount= litag.find('span', attrs={'class':'a-size-base a-color-price s-price a-text-bold'})
	ans=str(amount)
	a = [s for s in ans.split('</span>')]
	if len(a)>1:
		amounts = '-'.join([a[1].split('-')[0],a[2]])
	else:
		amounts = a[1] 
	print( "price:{a}".format(a=amounts))
	shoe_dict[s_id]={}
	shoe_dict[s_id]['title']=title
	shoe_dict[s_id]['img_url']=img_url
	shoe_dict[s_id]['price']=amounts

print (shoe_dict)

with open('names.csv', 'w') as csvfile:
	fieldnames = ['title', 'image_url','price']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for record in shoe_dict.keys():
		writer.writerow({'title':shoe_dict[record]['title'],'image_url':shoe_dict[record]['img_url'],'price':shoe_dict[record]['price']})
