import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time


ua = UserAgent()
header = { 'user-agent' : ua.chrome }



a= input("Enter the site you want soup for (eg. www.yahoo.com :   ")

try:
	url = requests.get( "https://" + a, headers=header)

	soup = BeautifulSoup(url.text, 'lxml')

	print(soup.prettify())

except:
	print("Incorrect format, let me make soup of Google")
	time.sleep(2)

	url = requests.get("https://www.google.com", headers=header)

	soup = BeautifulSoup(url.text, 'lxml')

	print(soup.prettify())


