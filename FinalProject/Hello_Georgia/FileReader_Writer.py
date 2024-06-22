import json


with open('../Region_Descriptions.json', 'r') as file:
    data = json.load(file)
aaa = "sadadasd"
def get_region_description(region):
    return data[region]

