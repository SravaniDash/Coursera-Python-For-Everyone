# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will
# prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON
# data, compute the sum of the numbers in the file and enter the sum belowself.
# Actual Data: http://py4e-data.dr-chuck.net/comments_1012758.json

import urllib.request, urllib.parse, urllib.error
import json

sum = 0
serviceurl = input("Enter url: ")

uh = urllib.request.urlopen(serviceurl)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)

for item in js["comments"]:
    num = item["count"]
    sum = sum + num
print("Sum:", sum)
