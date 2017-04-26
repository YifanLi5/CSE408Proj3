from PIL import Image
import emoji_json_parsing
import nearest_neighbor
from color_averaging import calc_avg_img_values
from emoji_json_parsing import rgb_tuple
path = "./TestImages/emoji_sheet.png"

def main():

    im = Image.open(path)
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    for i in range(height):
        for j in range(width):
            pixels[i][j] = emoji_json_parsing.rgb_tuple(*pixels[i][j])

    rgb_to_color_dict = emoji_json_parsing.parse()

    averaged_image = calc_avg_img_values(pixels, 64)




    # test_tup = rgb_tuple(r=84, g=139, b=91)
    #
    # result_tup = nearest_neighbor.first_nn(test_tup, rgb_to_color_dict)
    # color = rgb_to_color_dict[result_tup]
    # print(result_tup)
    # print(color)




def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


if __name__ == "__main__": main()

