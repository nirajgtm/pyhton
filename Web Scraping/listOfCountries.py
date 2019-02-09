import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import re


ua = UserAgent()
header = { 'user-agent' : ua.chrome }

try:
	url = requests.get("https://www.britannica.com/topic/list-of-countries-1993160", headers=header)

	soup = BeautifulSoup(url.text, 'lxml')

	attr = { 'class' : 'md-crosslink'}



	a= soup.find_all(attrs = attr)
	#find_all takes following arguements
	#name
	#attrs
	#recursive
	#string
	#**kwarfs

	# we can also use find function which returns the first object it finds
	i = 1

	b= input ("Enter the initials for countries (press Enter to list all countries) :  " ).upper()
	regex= re.compile("^" + b) 
	for items in a :
		country = (items.find_all( string = regex))
		if ( country != [] ):
			print( str(i) + ".  " + country[0] + "\n")
			i += 1
			if (i % 10 == 0) :
				time.sleep(1)


except:
	print("cant fetch data, inform author")