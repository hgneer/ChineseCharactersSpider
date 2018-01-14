# -*- coding: utf-8 -*-

from PIL import Image
import os

def main():
    if(os.path.isdir(os.curdir+"//Pictures_Converted")):
        pass
    else:
        os.mkdir(os.curdir+"//Pictures_Converted")

    path = os.curdir+"//Pictures_Converted"
    files = os.listdir(path)
    number_throw = 0
    number = 0

    for file in files:
        fileopen = open(path + "//" + file,"rb")
        number += 1
        picture = Image.open(fileopen)
        print(number)
        if(picture.getpixel((0,0)) == 0):
            number_throw += 1
            print(file)
            print(picture.getpixel((0,0)))
            print(number,number_throw)
            fileopen.close()
            os.remove(path + "//" + file)

if __name__ == "__main__":
    main()

