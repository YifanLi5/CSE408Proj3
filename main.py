from PIL import Image
import color_json_handling
import nearest_neighbor
import color_averaging
from color_json_handling import rgb_tuple
path = "./TestImages/slack_emoji_sheet.png"

def main():

    im = Image.open(path)
    pixels = list(im.getdata())
    print (im.mode)
    print(pixels);

"""
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    # for i in range(height):
    #     for j in range(width):
    #         pixels[i][j] = color_json_handling.rgb_tuple._make(pixels[i][j])

    rgb_to_color_dict = color_json_handling.parse()
    
    result = color_averaging.calc_avg_img_values(pixels, 64)
    pretty_print(result)
    
    # black = rgb_tuple(r=0, g=0, b=0)
    # white = rgb_tuple(r=255, g=255, b=255)
    # row0 = [black, black, black, black]
    # row1 = [white, white, black, black]
    # row2 = [black, black, white, white]
    # row3 = [white, white, white, white]
    # row4 = [black, black, white, black]
    # test = []
    # test.append(row0)
    # test.append(row1)
    # test.append(row2)
    # test.append(row3)
    # test.append(row4)

    # result = color_averaging.calc_avg_img_values(test, 2)

    # pretty_print(test)
    # print('\n')
    # pretty_print(result)
"""

def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


if __name__ == "__main__": main()

