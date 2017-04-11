from PIL import Image

path = "./TestImages/magikarp.jpg"

def main():

    im = Image.open(path)
    pixels = list(im.getdata())
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    print(pixels)

if __name__ == "__main__": main()

