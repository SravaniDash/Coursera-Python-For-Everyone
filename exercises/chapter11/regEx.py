import re

count = 0
hand = open("regex_sum.txt")
lines = hand.read()
match = re.findall('[0-9]+', lines)
for i in match:
    number = int(i)
    count = count + number

print(count)
