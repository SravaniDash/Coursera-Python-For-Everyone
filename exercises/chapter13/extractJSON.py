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
