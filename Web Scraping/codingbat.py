import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import re


ua = UserAgent()
header = { 'user-agent' : ua.chrome }

url = requests.get("https://codingbat.com/java", headers=header)

soup = BeautifulSoup(url.text, 'lxml')

attr = { 'class' : 'summ'}



a= soup.find_all('div', attrs= attr)

i = 1

topic = [item.a.span.string for item in a]
link = [item.a["href"] for item in a]

for topics, links in zip(topic, link) :
	print(topics)
	print('=='*25)
	url2 = requests.get ("https://codingbat.com" + links)
	soup2 = BeautifulSoup(url2.text, 'lxml')
	attr = { 'width' : '200'}
	b= soup2.find_all(attrs = attr)
	for link in b:
		print("...........")
		print(link.a.string)
		print("...........")
		url3 = requests.get ("https://codingbat.com" + link.a['href'])
		soup3= BeautifulSoup(url3.text, 'lxml')
		attr = { 'class' : 'max2'}
		c= soup3.find_all('p', attrs = attr)
		print(c[0].string)
		print("\n\n\n\n")
		# time.sleep(1)















# except:
# 	print("cant fetch data, inform author")