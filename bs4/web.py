import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re
url = input('Enter - ')
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
n=list()
tags = soup('span')
for tag in tags:
   n.append(int(tag.contents[0]))
print(sum(n))
