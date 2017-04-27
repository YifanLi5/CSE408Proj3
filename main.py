from PIL import Image
import emoji_json_parsing
import nearest_neighbor
from color_averaging import calc_avg_img_values
path = "./TestImages/emoji_sheet.jpg"

def main():

    im = Image.open(path)
    im = im.convert("RGB")
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    for i in range(height):
        for j in range(width):
            pixels[i][j] = emoji_json_parsing.rgb_tuple(*pixels[i][j])

    rgb_to_color_dict = emoji_json_parsing.parse()

    averaged_image = calc_avg_img_values(pixels, 64)
    colors = []
    temp = []
    for i in range(-1, 34):
        temp.append(str(i))
    colors.append(temp)
    for i,line in enumerate(averaged_image):
        color_line = []
        color_line.append(i)
        for pix in line:
            result_tup = nearest_neighbor.first_nn(pix, rgb_to_color_dict)
            color_line.append(rgb_to_color_dict[result_tup])
        colors.append(color_line)

    pretty_print(colors)


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

