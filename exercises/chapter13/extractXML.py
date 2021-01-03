import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
sum=0

address = input('Enter location: ')
handle = urllib.request.urlopen(address).read()
tree = ET.fromstring(handle)



for count in tree.findall('comments/comment'):
    val = int(count.find('count').text)
    sum=sum+val

print(sum)
