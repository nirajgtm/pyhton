import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import re


ua = UserAgent()
header = { 'user-agent' : ua.chrome }


url = requests.get("https://www.britannica.com/topic/list-of-countries-1993160", headers=header)

soup = BeautifulSoup(url.text, 'lxml')  #create a soup

attr = { 'class' : 'md-crosslink'} # atrribute to be matched



a= soup.find_all(attrs = attr) # all data for which attributes are matched
i = 1  # iterator for indexing countries

b= input ("Enter the initials for countries (press Enter to list all countries) :  " ).upper()  #take input for initials and convert if to uppercase
regex= re.compile("^" + b) # regex for ecerything starting with the string stored in variable "b"
for items in a :			# for items matchinf our attributes
	country = (items.find_all( string = regex)) #apply regex
	if ( country != [] ): #if the country is not empty 
		print( str(i) + ".  " + country[0] + "\n") #print country name
		i += 1
		if (i % 10 == 0) :
			time.sleep(1)			#delay so that user can read the data


