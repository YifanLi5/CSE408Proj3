from PIL import Image
import emoji_json_parsing
import nearest_neighbor
import emoji
from color_averaging import calc_avg_img_values
path = "./TestImages/magikarp.png"

def main():
    print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
    # im = Image.open(path)
    # im = im.convert("RGB")
    # pixels = list(im.getdata())
    # width, height = im.size
    # pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    # for i in range(height):
    #     for j in range(width):
    #         pixels[i][j] = emoji_json_parsing.rgb_tuple(*pixels[i][j])
    # #get dict (key: rgb_tuple, value: slack_code)
    # rgb_to_slack_code = emoji_json_parsing.parse()

    # averaged_image = calc_avg_img_values(pixels, 5)
    # slack_emoji_image = []
    # for line in averaged_image:
    #     slack_emoji_line = []
    #     for pix in line:
    #         #for every pixel in input image, get closest colored emoji from emojis.json
    #         #then put into 2d list so every emoji represents sq_length^2 pixels
    #         result_tup = nearest_neighbor.first_nn(pix, rgb_to_slack_code)
    #         slack_emoji_line.append(rgb_to_slack_code[result_tup])
    #     slack_emoji_image.append(slack_emoji_line)

    # #pretty_print(slack_emoji_image)
    # slack_printer(slack_emoji_image)


    # test_tup = rgb_tuple(r=84, g=139, b=91)
    #
    # result_tup = nearest_neighbor.first_nn(test_tup, rgb_to_slack_code)
    # color = rgb_to_slack_code[result_tup]
    # print(result_tup)
    # print(color)


def slack_printer(matrix):
    #for line in matrix:
    #    for pix in line:
    #        print(pix, end='')
        print()

def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


if __name__ == "__main__": main()

