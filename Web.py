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

# step =1 get the html
r = requests.get(url)
htmlContent = r.content	# r returns response so if we want the code we write r.content
print(htmlContent)		# printing the code

# step 2 : Parse the htmlContent
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())   # ✅ added () here

# step3 :HTML Tree traversal
# commonly used types of objects in bs4
# 1.Tag
# 2.NavigableString
# 3.BeautifulSoup
# 4.Comment

#Get the title of the HTML page
title = soup.title

# Get all the paragraph from the page
paras = soup.find_all('p')
print(paras)
