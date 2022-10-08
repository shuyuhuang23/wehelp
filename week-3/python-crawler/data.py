import requests
import json
import csv
import re

def parse_area(address):
    end_idx = address.find('區')
    return address[end_idx - 2: end_idx + 1]

def parse_first_img(img_str):
    iter = re.finditer('http', img_str)
    for i, find_result in enumerate(iter):
        if i == 1:
            return img_str[0: find_result.start()]

def get_data_by_year(data, year):
    result = []
    if int(data['xpostDate'][0:4]) >= year:
        result.append(data['stitle'])
        result.append(parse_area(data['address']))
        result.append(data['longitude'])
        result.append(data['latitude'])
        result.append(parse_first_img(data['file']))
    return result

response = requests.get("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
attractions = json.loads(response.text)['result']['results']
output = []
for item in attractions:
    save_item = get_data_by_year(item, 2015)
    if len(save_item) != 0:
        output.append(save_item)

with open('data.csv', 'w') as  f:
    writer = csv.writer(f)
    writer.writerows(output)
