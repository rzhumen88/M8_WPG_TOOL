import os
from PIL import Image


def pack_wpk(filename, images_dir):
    with open(filename, 'wb') as wpg:
        images = os.listdir(images_dir)
        wpg.write(b'wpg')
        wpg.write(b'\x00' * 29)
        for img in images:
            img = Image.open(images_dir+"/"+img)
            wpg.write(b'\x00'*2)
            wpg.write(b'\x02')
            wpg.write(b'\x00'*9)
            wpg.write(int.to_bytes(img.width, 2, byteorder='little'))
            wpg.write(int.to_bytes(img.height, 2, byteorder='little'))
            wpg.write(b'\x20\x08')
            for y in range(img.height):
                for x in range(img.width):
                    r, g, b, a = img.getpixel((x, y))
                    b = int.to_bytes(b, 1)
                    g = int.to_bytes(g, 1)
                    r = int.to_bytes(r, 1)
                    a = int.to_bytes(a, 1)
                    wpg.write(b + g + r + a)
    print(filename+ " created!")


if __name__ == "__main__":
    filename = ""
    images_dir = ""
    while not os.path.isdir(images_dir):
        images_dir = input("Input path to the folder with textures:   ")
    filename = images_dir + ".wpg"
    pack_wpk(filename, images_dir)
    input()
