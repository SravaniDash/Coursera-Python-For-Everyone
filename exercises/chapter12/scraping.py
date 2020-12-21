# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use
# urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers
# in the file.
# Data: http://py4e-data.dr-chuck.net/comments_1012755.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum=0
tags = soup('span') # Retrieve all of the span tags

for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)
