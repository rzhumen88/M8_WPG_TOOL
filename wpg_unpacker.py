#wpg unpacker - Megaman x8 PC

import os
from PIL import Image

def parse_textures(file):
    with open(file, 'rb') as f:
        f = f.read()
        if f[:3] != b'wpg':
            print("Error: not a wpg file or header is incorrect")
        f = f[32:]
        i = 0
        textures = []
        while len(f) > 0:
            unk_1 = f[:4]
            width = int.from_bytes(f[12:14], byteorder='little')
            heigth = int.from_bytes(f[14:16], byteorder='little')
            unk_2 = f[16:18]
            rgba = f[18:18+width*heigth*4]
            textures.append((width,heigth,rgba))
            f = f[18+width*heigth*4:]
            i += 1
        print(f"Found {i} textures!")
    return textures

def save_textures(file, textures):
    name = 0
    dir_ = file[:-4]+"/"
    for t in textures:
        name += 1
        width = t[0]
        heigth = t[1]
        rgba = t[2]
        i = 0
        texture = Image.new('RGBA', (width, heigth), color=(0,0,0,0))
        for y in range(heigth):
            for x in range(width):
                b = rgba[i]
                g = rgba[i+1]
                r = rgba[i+2]
                a = rgba[i+3]
                i += 4
                texture.putpixel((x,y), (r,g,b,a))
        if not os.path.isdir(dir_):
            os.mkdir(dir_)
        texture.save(dir_+str(name)+".png")
        print(dir_+str(name)+".png")


if __name__ == "__main__":
    while True:
        file = ""
        while not os.path.isfile(file):
            print("-"*30)
            print("Input path to wpg file:   ")
            file = input()
        textures = parse_textures(file)
        save_textures(file, textures)
