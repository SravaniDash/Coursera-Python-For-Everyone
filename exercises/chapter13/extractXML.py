# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will
# prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file.
# Actual Data: http://py4e-data.dr-chuck.net/comments_1012757.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum=0

address = input('Enter location: ')
handle = urllib.request.urlopen(address).read()
tree = ET.fromstring(handle)


for count in tree.findall('comments/comment'):
    val = int(count.find('count').text)
    sum = sum + val

print(sum)
