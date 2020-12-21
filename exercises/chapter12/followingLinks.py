# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will
# use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is
# in a particular position relative to the first name in the list, follow that link and repeat the process a number of times
# and report the last name you find.
# Data: Start at: http://py4e-data.dr-chuck.net/known_by_Hollee.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name
# that you retrieve.
# Hint: The first character of the name of the last page that you will load is: R

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input("Enter position: "))-1
count = int(input("Enter count: "))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

Sequence = []
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])
