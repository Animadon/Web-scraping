#if you wANT TO SCRAPE A WEBSITE 
# 1.use THE API
# HTML Web Scraping using tool like bs4
# step =0 install all the requirements 
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
r = requests.get(url)
# step =1 get the html
htmlContent = r.content	# r returns response so if we want the code we write r.content
# print(htmlContent)
#step 2
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())	# to print html in tree structure
	# printing the code
title = soup.title
print(type(title.string))	# to print the title of the page in string format
