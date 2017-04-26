import json
import emoji_json_parsing
import nearest_neighbor

filepath_selected_emojis = "./emojis.json"

def main():
    rgb_to_color_dict = emoji_json_parsing.parse()
    with open(filepath_selected_emojis) as raw_data:
        json_data = json.load(raw_data)

    for rgb_item in json_data:
        tup = emoji_json_parsing.rgb_tuple(r=rgb_item["x"], g=rgb_item["y"], b=rgb_item["z"])
        nn = nearest_neighbor.first_nn(tup, rgb_to_color_dict)
        print("slack_code: " + rgb_item["slack_code"] + "\tclosest_color: " + str(rgb_to_color_dict[nn]) + "\t1nn_rgb: " + str(nn))
        #asldlkfjaslk;dfj

if __name__ == "__main__": main()