import json
from collections import namedtuple

filepath = "./emoji_list.json"
rgb_tuple = namedtuple("rgb_tuple", ["r", "g", "b", "a"])

def parse():
    with open(filepath) as raw_data:
        json_data = json.load(raw_data)

    rgb_to_color_dict = {}
    for rgb_item in json_data:
        tup = rgb_tuple(r = rgb_item["x"], g = rgb_item["y"], b = rgb_item["z"], a = -1)
        label = rgb_item["label"]
        rgb_to_color_dict[tup] = label
    return rgb_to_color_dict

