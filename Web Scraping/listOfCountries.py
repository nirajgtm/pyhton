import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import re

ua = UserAgent()
header = { 'user-agent' : ua.chrome }


url = requests.get("https://www.britannica.com/topic/list-of-countries-1993160", headers=header)

soup = BeautifulSoup(url.text, 'lxml')

attr = { 'class' : 'md-crosslink'}



a= soup.find_all(attrs = attr)
i = 0

print("Following is the list of all the countries in the world")
for items in a :
	print( str(i) + ".  " + items.text + "\n")
	i += 1
