import json
from collections import namedtuple

filepath = "./color_json.js"
rgb_tuple = namedtuple("rgb_tuple", ["r", "g", "b"])

def parse():
    with open(filepath) as raw_data:
        json_data = json.load(raw_data)

    rgb_to_color_dict = {}
    for rgb_item in json_data:
        tup = rgb_tuple(r = rgb_item["x"], g = rgb_item["y"], b = rgb_item["z"])
        label = rgb_item["label"]
        rgb_to_color_dict[tup] = label
    return rgb_to_color_dict

# dict = parse()
# test_tup = rgb_tuple(r = 240, g = 248, b = 255)
# print(dict[test_tup])
