from PIL import Image
import color_json_handling
import nearest_neighbor
from color_json_handling import rgb_tuple
path = "./TestImages/magikarp.jpg"

def main():

    im = Image.open(path)
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    for i in range(height):
        for j in range(width):
            pixels[i][j] = color_json_handling.rgb_tuple(*pixels[i][j])

    rgb_to_color_dict = color_json_handling.parse()
    test_tup = rgb_tuple(r=84, g=139, b=91)

    result_tup = nearest_neighbor.first_nn(test_tup, rgb_to_color_dict)
    color = rgb_to_color_dict[result_tup]
    print(result_tup)
    print(color)



if __name__ == "__main__": main()

