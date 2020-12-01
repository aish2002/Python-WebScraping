import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re
url=input("Enter URL:")
c=input("Enter count:")
p=input("Enter position:")
try:
    c1=int(c)
    p1=int(p)
except:
    pass
f=urllib.request.urlopen(url)
print("Retrieving:",url)
e=f
for i in range (0,c1):
    soup = BeautifulSoup(e, "html.parser")
    tags=soup('a')
    a=tags[p1-1].get("href",None)
    print("Retrieving:",a)
    e=urllib.request.urlopen(a)
'''for i in tags:
    a=i.get("href",None)
    print("Retrieving:",a)
    for j in i:
        a=(re.findall('^[A-Z]\S*^.',j))
        for k in a:
              count+=1
        


for i in f:
    print(i.decode())'''