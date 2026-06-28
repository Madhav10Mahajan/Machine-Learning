# python standard lubrary is vast collection of modules and packages
# that come bundled with python providing wide range of functionalities out of the box

import array
arr=array.array('i',[1,2,3])
print(arr)

import math
print(math.pi)
print(math.sqrt(4))

import random
print(random.randint(1,10)) # returns a random numbr bw 1 to 10 including both
print(random.choice(['apple','banana','cherry']))

import json
data={'name':'madhav', 'age':23}

json_str=json.dumps(data)
print(json_str)
print(type(json_str))
parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

import csv
with open('data.csv', mode='w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['madhav',23])
    writer.writerow(['rohit',24])

with open('data.csv', mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)

## time
import time
print(time.time())
time.sleep(2)
print(time.time())

## regular expression matching

import re
pattern=r'\d +'
text='there are 123 appled'
match=re.search(pattern,text)
print(match.group())