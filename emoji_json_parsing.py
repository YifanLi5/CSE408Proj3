import json
from collections import namedtuple

filepath = "./emojis.json"
rgb_tuple = namedtuple("rgb_tuple", ["r", "g", "b"])


def parse():
    with open(filepath) as raw_data:
        json_data = json.load(raw_data)

    rgb_to_slack_code = {}
    for rgb_item in json_data:
        tup = rgb_tuple(r=rgb_item["x"], g=rgb_item["y"], b=rgb_item["z"])
        slack_code = str(rgb_item["slack_code"])
        rgb_to_slack_code[tup] = slack_code
    return rgb_to_slack_code
